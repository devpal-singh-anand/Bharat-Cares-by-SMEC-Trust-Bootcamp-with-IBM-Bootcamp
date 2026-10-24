"""
StreamSafe ADS Tool
-------------------
A Windows-only GUI tool for creating, listing, reading and deleting
NTFS Alternate Data Streams on any file, folder or ZIP archive.

Author  : Devpal Singh Charanjeet Singh Anand
Project : IBM SkillsBuild Cyber Security BootCamp 2026 — BharatCares
License : Apache 2.0
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import ctypes
from ctypes import wintypes
import hashlib
import os
import sys
import datetime
import threading

# ─── Windows API setup ────────────────────────────────────────────────────────

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

GENERIC_READ        = 0x80000000
GENERIC_WRITE       = 0x40000000
OPEN_ALWAYS         = 4
OPEN_EXISTING       = 3
CREATE_ALWAYS       = 2
FILE_SHARE_READ     = 0x00000001
FILE_SHARE_WRITE    = 0x00000002
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000   # required for folders
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

class WIN32_FIND_STREAM_DATA(ctypes.Structure):
    _fields_ = [
        ("StreamSize", wintypes.LARGE_INTEGER),
        ("cStreamName", ctypes.c_wchar * 296),
    ]

kernel32.CreateFileW.restype  = wintypes.HANDLE
kernel32.CreateFileW.argtypes = [
    wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
    ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
]
kernel32.WriteFile.restype  = wintypes.BOOL
kernel32.WriteFile.argtypes = [
    wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD), ctypes.c_void_p,
]
kernel32.ReadFile.restype  = wintypes.BOOL
kernel32.ReadFile.argtypes = [
    wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD), ctypes.c_void_p,
]
kernel32.CloseHandle.restype  = wintypes.BOOL
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.FindFirstStreamW.restype  = wintypes.HANDLE
kernel32.FindFirstStreamW.argtypes = [
    wintypes.LPCWSTR, wintypes.DWORD, ctypes.POINTER(WIN32_FIND_STREAM_DATA), wintypes.DWORD,
]
kernel32.FindNextStreamW.restype  = wintypes.BOOL
kernel32.FindNextStreamW.argtypes = [
    wintypes.HANDLE, ctypes.POINTER(WIN32_FIND_STREAM_DATA),
]
kernel32.FindClose.restype  = wintypes.BOOL
kernel32.FindClose.argtypes = [wintypes.HANDLE]
kernel32.DeleteFileW.restype  = wintypes.BOOL
kernel32.DeleteFileW.argtypes = [wintypes.LPCWSTR]
kernel32.GetFileSizeEx.restype  = wintypes.BOOL
kernel32.GetFileSizeEx.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.LARGE_INTEGER)]

# ─── ADS Core Functions ───────────────────────────────────────────────────────

def ads_write(target_path: str, stream_name: str, content: bytes) -> dict:
    """Write content to an ADS stream. Returns info dict."""
    stream_path = f"{target_path}:{stream_name}"
    flags = FILE_FLAG_BACKUP_SEMANTICS if os.path.isdir(target_path) else 0
    handle = kernel32.CreateFileW(
        stream_path,
        GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        None,
        CREATE_ALWAYS,
        flags,
        None,
    )
    if handle == INVALID_HANDLE_VALUE:
        err = ctypes.get_last_error()
        raise OSError(f"CreateFileW failed (error {err}): {ctypes.FormatError(err)}")
    try:
        written = wintypes.DWORD(0)
        buf = ctypes.create_string_buffer(content)
        ok = kernel32.WriteFile(handle, buf, len(content), ctypes.byref(written), None)
        if not ok:
            err = ctypes.get_last_error()
            raise OSError(f"WriteFile failed (error {err}): {ctypes.FormatError(err)}")
        sha256 = hashlib.sha256(content).hexdigest()
        return {"stream": stream_name, "bytes_written": written.value, "sha256": sha256}
    finally:
        kernel32.CloseHandle(handle)


def ads_read(target_path: str, stream_name: str) -> bytes:
    """Read content from an ADS stream."""
    stream_path = f"{target_path}:{stream_name}"
    flags = FILE_FLAG_BACKUP_SEMANTICS if os.path.isdir(target_path) else 0
    handle = kernel32.CreateFileW(
        stream_path,
        GENERIC_READ,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        None,
        OPEN_EXISTING,
        flags,
        None,
    )
    if handle == INVALID_HANDLE_VALUE:
        err = ctypes.get_last_error()
        raise OSError(f"Cannot open stream (error {err}): {ctypes.FormatError(err)}")
    try:
        size = wintypes.LARGE_INTEGER(0)
        kernel32.GetFileSizeEx(handle, ctypes.byref(size))
        file_size = size.value
        if file_size == 0:
            return b""
        buf = ctypes.create_string_buffer(file_size)
        read = wintypes.DWORD(0)
        kernel32.ReadFile(handle, buf, file_size, ctypes.byref(read), None)
        return buf.raw[:read.value]
    finally:
        kernel32.CloseHandle(handle)


def ads_list(target_path: str) -> list:
    """List all ADS streams on a file or folder."""
    data = WIN32_FIND_STREAM_DATA()
    handle = kernel32.FindFirstStreamW(target_path, 0, ctypes.byref(data), 0)
    streams = []
    if handle == INVALID_HANDLE_VALUE:
        return streams
    try:
        while True:
            name = data.cStreamName
            size = data.StreamSize
            # Skip the default data stream
            if name not in ("::$DATA", ":$DATA"):
                # Strip :$DATA suffix → bare name
                bare = name.lstrip(":").replace(":$DATA", "")
                streams.append({"name": bare, "size": size, "raw": name})
            if not kernel32.FindNextStreamW(handle, ctypes.byref(data)):
                break
    finally:
        kernel32.FindClose(handle)
    return streams


def ads_delete(target_path: str, stream_name: str):
    """Delete an ADS stream."""
    stream_path = f"{target_path}:{stream_name}:$DATA"
    ok = kernel32.DeleteFileW(stream_path)
    if not ok:
        # try without $DATA suffix
        ok = kernel32.DeleteFileW(f"{target_path}:{stream_name}")
    if not ok:
        err = ctypes.get_last_error()
        raise OSError(f"DeleteFile failed (error {err}): {ctypes.FormatError(err)}")


# ─── GUI App ──────────────────────────────────────────────────────────────────

DARK_BG      = "#1e1e2e"
PANEL_BG     = "#2a2a3e"
ACCENT       = "#7c3aed"
ACCENT_HOVER = "#6d28d9"
TEXT         = "#e2e8f0"
MUTED        = "#94a3b8"
SUCCESS      = "#22c55e"
ERROR        = "#ef4444"
WARNING      = "#f59e0b"
CONSOLE_BG   = "#0f0f1a"
CONSOLE_FG   = "#a0e9a0"
BORDER       = "#3f3f5a"

FONT_MAIN    = ("Segoe UI", 10)
FONT_BOLD    = ("Segoe UI", 10, "bold")
FONT_TITLE   = ("Segoe UI", 16, "bold")
FONT_MONO    = ("Consolas", 9)


class StreamSafeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StreamSafe ADS Tool")
        self.geometry("900x700")
        self.minsize(800, 600)
        self.configure(bg=DARK_BG)
        self.resizable(True, True)

        # State
        self.selected_path = tk.StringVar(value="")
        self.stream_name   = tk.StringVar(value="")
        self.selected_stream_for_read = tk.StringVar(value="")

        self._build_ui()
        self._log("StreamSafe ADS Tool ready.", "info")
        self._log("Select a file, folder, or ZIP to get started.", "muted")
        self._log("─" * 60, "muted")

    # ── Build UI ──────────────────────────────────────────────────

    def _build_ui(self):
        # Title bar
        title_frame = tk.Frame(self, bg=ACCENT, pady=10)
        title_frame.pack(fill="x")
        tk.Label(title_frame, text="🔒  StreamSafe ADS Tool",
                 font=FONT_TITLE, bg=ACCENT, fg="white").pack(side="left", padx=16)
        tk.Label(title_frame, text="NTFS Alternate Data Stream Manager",
                 font=FONT_MAIN, bg=ACCENT, fg="#ddd6fe").pack(side="left", padx=4)

        # Main body
        body = tk.Frame(self, bg=DARK_BG)
        body.pack(fill="both", expand=True, padx=16, pady=12)

        # Left column: controls
        left = tk.Frame(body, bg=DARK_BG)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        # Right column: stream list
        right = tk.Frame(body, bg=PANEL_BG, bd=0, relief="flat",
                         highlightbackground=BORDER, highlightthickness=1)
        right.pack(side="right", fill="both", expand=False, ipadx=8, ipady=8)
        right.configure(width=240)
        right.pack_propagate(False)

        self._build_target_section(left)
        self._build_write_section(left)
        self._build_read_section(left)
        self._build_stream_list_panel(right)
        self._build_console(self)

    def _section(self, parent, title):
        frame = tk.Frame(parent, bg=PANEL_BG,
                         highlightbackground=BORDER, highlightthickness=1)
        frame.pack(fill="x", pady=(0, 10))
        tk.Label(frame, text=title, font=FONT_BOLD,
                 bg=PANEL_BG, fg=ACCENT).pack(anchor="w", padx=12, pady=(8, 4))
        inner = tk.Frame(frame, bg=PANEL_BG)
        inner.pack(fill="x", padx=12, pady=(0, 10))
        return inner

    def _build_target_section(self, parent):
        inner = self._section(parent, "① Select Target")

        tk.Label(inner, text="Path (file / folder / ZIP):",
                 font=FONT_MAIN, bg=PANEL_BG, fg=MUTED).pack(anchor="w")

        row = tk.Frame(inner, bg=PANEL_BG)
        row.pack(fill="x", pady=(2, 6))

        path_entry = tk.Entry(row, textvariable=self.selected_path,
                              font=FONT_MONO, bg="#12121f", fg=TEXT,
                              insertbackground=TEXT, relief="flat",
                              highlightbackground=BORDER, highlightthickness=1)
        path_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 6))

        btn_row = tk.Frame(inner, bg=PANEL_BG)
        btn_row.pack(fill="x")
        self._btn(btn_row, "📄 File",   self._pick_file,   ACCENT).pack(side="left", padx=(0,4))
        self._btn(btn_row, "📁 Folder", self._pick_folder, "#0891b2").pack(side="left", padx=(0,4))
        self._btn(btn_row, "🗜 ZIP",    self._pick_zip,    "#059669").pack(side="left")
        self._btn(btn_row, "🔄 Refresh Streams", self._refresh_streams, "#64748b").pack(side="right")

    def _build_write_section(self, parent):
        inner = self._section(parent, "② Create / Write Stream")

        tk.Label(inner, text="Stream Name:", font=FONT_MAIN, bg=PANEL_BG, fg=MUTED).pack(anchor="w")
        tk.Entry(inner, textvariable=self.stream_name,
                 font=FONT_MONO, bg="#12121f", fg=TEXT,
                 insertbackground=TEXT, relief="flat",
                 highlightbackground=BORDER, highlightthickness=1,
                 width=30).pack(anchor="w", ipady=5, pady=(2,8), fill="x")

        tk.Label(inner, text="Stream Content:", font=FONT_MAIN, bg=PANEL_BG, fg=MUTED).pack(anchor="w")
        self.content_text = tk.Text(inner, height=5, font=FONT_MONO,
                                    bg="#12121f", fg=TEXT, insertbackground=TEXT,
                                    relief="flat",
                                    highlightbackground=BORDER, highlightthickness=1,
                                    wrap="word")
        self.content_text.pack(fill="x", pady=(2, 8))

        btn_row = tk.Frame(inner, bg=PANEL_BG)
        btn_row.pack(fill="x")
        self._btn(btn_row, "✅ Write Stream", self._write_stream, SUCCESS, fg="black").pack(side="left", padx=(0,6))
        self._btn(btn_row, "🗑 Delete Stream", self._delete_stream, ERROR).pack(side="left")
        self._btn(btn_row, "🧹 Clear", self._clear_write, "#64748b").pack(side="right")

    def _build_read_section(self, parent):
        inner = self._section(parent, "③ Read Stream")

        tk.Label(inner, text="Stream Name to Read:",
                 font=FONT_MAIN, bg=PANEL_BG, fg=MUTED).pack(anchor="w")

        row = tk.Frame(inner, bg=PANEL_BG)
        row.pack(fill="x", pady=(2, 6))

        tk.Entry(row, textvariable=self.selected_stream_for_read,
                 font=FONT_MONO, bg="#12121f", fg=TEXT,
                 insertbackground=TEXT, relief="flat",
                 highlightbackground=BORDER, highlightthickness=1).pack(
                     side="left", fill="x", expand=True, ipady=5, padx=(0,6))

        self._btn(row, "📖 Read", self._read_stream, "#0891b2").pack(side="left")

    def _build_stream_list_panel(self, parent):
        tk.Label(parent, text="📋 Streams on Target",
                 font=FONT_BOLD, bg=PANEL_BG, fg=ACCENT).pack(anchor="w", padx=10, pady=(10,4))

        tk.Label(parent, text="Click a stream to select it",
                 font=("Segoe UI", 8), bg=PANEL_BG, fg=MUTED).pack(anchor="w", padx=10)

        list_frame = tk.Frame(parent, bg=PANEL_BG)
        list_frame.pack(fill="both", expand=True, padx=10, pady=6)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.stream_listbox = tk.Listbox(
            list_frame, yscrollcommand=scrollbar.set,
            bg=CONSOLE_BG, fg=CONSOLE_FG, selectbackground=ACCENT,
            selectforeground="white", font=FONT_MONO,
            relief="flat", borderwidth=0, activestyle="none",
        )
        self.stream_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.stream_listbox.yview)
        self.stream_listbox.bind("<<ListboxSelect>>", self._on_stream_select)

        btn_frame = tk.Frame(parent, bg=PANEL_BG)
        btn_frame.pack(fill="x", padx=10, pady=(0,10))
        self._btn(btn_frame, "🔄", self._refresh_streams, "#64748b", width=3).pack(side="right")

    def _build_console(self, parent):
        console_outer = tk.Frame(parent, bg=DARK_BG)
        console_outer.pack(fill="x", padx=16, pady=(0,12))

        header = tk.Frame(console_outer, bg="#0f0f1a")
        header.pack(fill="x")
        tk.Label(header, text="⬛  Console Output", font=FONT_BOLD,
                 bg="#0f0f1a", fg=MUTED).pack(side="left", padx=10, pady=4)
        self._btn(header, "Clear Console", self._clear_console, "#374151", pady=2).pack(side="right", padx=6, pady=4)

        self.console = scrolledtext.ScrolledText(
            console_outer, height=10, font=FONT_MONO,
            bg=CONSOLE_BG, fg=CONSOLE_FG,
            insertbackground=CONSOLE_FG,
            relief="flat", state="disabled",
            highlightbackground=BORDER, highlightthickness=1,
        )
        self.console.pack(fill="x")

        # Tag colours
        self.console.tag_config("info",    foreground="#a0e9a0")
        self.console.tag_config("success", foreground="#22c55e")
        self.console.tag_config("error",   foreground="#ef4444")
        self.console.tag_config("warning", foreground="#f59e0b")
        self.console.tag_config("muted",   foreground="#64748b")
        self.console.tag_config("data",    foreground="#60a5fa")
        self.console.tag_config("hash",    foreground="#c084fc")

    # ── Widget Helpers ────────────────────────────────────────────

    def _btn(self, parent, text, cmd, bg, fg="white", width=None, pady=4):
        kwargs = dict(text=text, command=cmd, bg=bg, fg=fg,
                      font=FONT_BOLD, relief="flat", cursor="hand2",
                      padx=10, pady=pady, activebackground=ACCENT_HOVER,
                      activeforeground="white", bd=0)
        if width:
            kwargs["width"] = width
        return tk.Button(parent, **kwargs)

    # ── File Picking ──────────────────────────────────────────────

    def _pick_file(self):
        p = filedialog.askopenfilename(title="Select a file")
        if p:
            self.selected_path.set(p)
            self._log(f"Selected file: {p}", "info")
            self._refresh_streams()

    def _pick_folder(self):
        p = filedialog.askdirectory(title="Select a folder")
        if p:
            self.selected_path.set(p)
            self._log(f"Selected folder: {p}", "info")
            self._refresh_streams()

    def _pick_zip(self):
        p = filedialog.askopenfilename(
            title="Select a ZIP file",
            filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
        )
        if p:
            self.selected_path.set(p)
            self._log(f"Selected ZIP: {p}", "info")
            self._refresh_streams()

    # ── Core Actions ──────────────────────────────────────────────

    def _write_stream(self):
        path    = self.selected_path.get().strip()
        name    = self.stream_name.get().strip()
        content = self.content_text.get("1.0", "end-1c")

        if not path:
            self._log("❌ No target selected.", "error"); return
        if not name:
            self._log("❌ Stream name is required.", "error"); return
        if not os.path.exists(path):
            self._log(f"❌ Path does not exist: {path}", "error"); return

        def _do():
            try:
                data = content.encode("utf-8")
                ts   = datetime.datetime.now().strftime("%H:%M:%S")
                self._log(f"[{ts}] Writing stream '{name}' → {path}", "info")
                result = ads_write(path, name, data)
                self._log(f"✅ Stream written successfully!", "success")
                self._log(f"   Bytes written : {result['bytes_written']}", "data")
                self._log(f"   SHA-256       : {result['sha256']}", "hash")
                self._log("─" * 60, "muted")
                self.after(0, self._refresh_streams)
            except Exception as e:
                self._log(f"❌ Error: {e}", "error")

        threading.Thread(target=_do, daemon=True).start()

    def _read_stream(self):
        path = self.selected_path.get().strip()
        name = self.selected_stream_for_read.get().strip()

        if not path:
            self._log("❌ No target selected.", "error"); return
        if not name:
            self._log("❌ Enter a stream name to read.", "error"); return

        def _do():
            try:
                ts = datetime.datetime.now().strftime("%H:%M:%S")
                self._log(f"[{ts}] Reading stream '{name}' from: {path}", "info")
                data = ads_read(path, name)
                sha  = hashlib.sha256(data).hexdigest()
                self._log(f"✅ Stream read successfully!", "success")
                self._log(f"   Size   : {len(data)} bytes", "data")
                self._log(f"   SHA-256: {sha}", "hash")
                try:
                    text = data.decode("utf-8")
                    self._log(f"   Content: {text[:500]}", "data")
                except UnicodeDecodeError:
                    self._log(f"   Content: <binary data — {len(data)} bytes>", "warning")
                self._log("─" * 60, "muted")
            except Exception as e:
                self._log(f"❌ Error: {e}", "error")

        threading.Thread(target=_do, daemon=True).start()

    def _delete_stream(self):
        path = self.selected_path.get().strip()
        name = self.stream_name.get().strip()

        if not path or not name:
            self._log("❌ Select a target and enter a stream name to delete.", "error"); return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete stream '{name}' from:\n{path}\n\nThis cannot be undone."
        )
        if not confirm:
            return

        def _do():
            try:
                ts = datetime.datetime.now().strftime("%H:%M:%S")
                self._log(f"[{ts}] Deleting stream '{name}' from: {path}", "warning")
                ads_delete(path, name)
                self._log(f"✅ Stream '{name}' deleted.", "success")
                self._log("─" * 60, "muted")
                self.after(0, self._refresh_streams)
            except Exception as e:
                self._log(f"❌ Error: {e}", "error")

        threading.Thread(target=_do, daemon=True).start()

    def _refresh_streams(self):
        path = self.selected_path.get().strip()
        self.stream_listbox.delete(0, "end")

        if not path or not os.path.exists(path):
            self.stream_listbox.insert("end", "(no target selected)")
            return

        def _do():
            try:
                streams = ads_list(path)
                self.after(0, lambda: self._populate_stream_list(streams, path))
            except Exception as e:
                self._log(f"❌ Stream list error: {e}", "error")

        threading.Thread(target=_do, daemon=True).start()

    def _populate_stream_list(self, streams, path):
        self.stream_listbox.delete(0, "end")
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        if not streams:
            self.stream_listbox.insert("end", "(no ADS found)")
            self._log(f"[{ts}] No alternate data streams found on: {path}", "muted")
        else:
            self._log(f"[{ts}] Found {len(streams)} stream(s) on: {path}", "info")
            for s in streams:
                display = f"{s['name']}  ({s['size']} B)"
                self.stream_listbox.insert("end", display)
                self._log(f"   📌 {s['name']}  —  {s['size']} bytes", "data")
            self._log("─" * 60, "muted")

    def _on_stream_select(self, event):
        sel = self.stream_listbox.curselection()
        if not sel:
            return
        item = self.stream_listbox.get(sel[0])
        # Extract bare name before the spaces
        bare = item.split("  ")[0].strip()
        if bare not in ("(no ADS found)", "(no target selected)"):
            self.stream_name.set(bare)
            self.selected_stream_for_read.set(bare)

    def _clear_write(self):
        self.stream_name.set("")
        self.content_text.delete("1.0", "end")

    def _clear_console(self):
        self.console.configure(state="normal")
        self.console.delete("1.0", "end")
        self.console.configure(state="disabled")

    # ── Logging ───────────────────────────────────────────────────

    def _log(self, msg: str, tag: str = "info"):
        def _append():
            self.console.configure(state="normal")
            self.console.insert("end", msg + "\n", tag)
            self.console.see("end")
            self.console.configure(state="disabled")
        self.after(0, _append)


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if sys.platform != "win32":
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Windows Only",
            "NTFS Alternate Data Streams are a Windows-only feature.\n"
            "Please run this tool on Windows 10 or Windows 11."
        )
        sys.exit(1)

    app = StreamSafeApp()
    app.mainloop()
