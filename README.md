# StreamSafe — NTFS Forensics & ADS Archiver Toolkit

> IBM SkillsBuild Cyber Security BootCamp 2026 · BharatCares / Renalysis Consultants Pvt. Ltd.

---

## About

StreamSafe is a complete digital forensics toolkit for Windows, built around a capability no mainstream archiver provides — **NTFS Alternate Data Stream (ADS) preservation**.

When you archive a file with 7-Zip, WinRAR, or Windows ZIP, all hidden ADS streams are silently dropped with no warning. For forensic investigators, this means critical metadata, origin markers (`Zone.Identifier`), and attacker-planted payloads vanish from evidence without a trace.

StreamSafe solves this with two complementary tools:

- **StreamSafe Desktop** — a full-featured forensic archiver built with Tauri v2 (Rust + React)
- **Python ADS Tool** (`app.py`) — a zero-dependency GUI for direct ADS inspection and manipulation

---

## Downloads

The latest release is available under [Releases](../../releases).

| File | Type | Size |
|------|------|------|
| `StreamSafe_0.1.0_x64_en-US.msi` | Windows Installer (MSI) | ~6.7 MB |
| `StreamSafe_0.1.0_x64-setup.exe` | NSIS Setup Wizard | ~4.9 MB |

> **Requirements:** Windows 10 / 11 · x64 · NTFS volume

---

## Features

### StreamSafe Desktop Application
- **ADS-Aware Archiving** — preserves all NTFS Alternate Data Streams inside standard archive formats using a structured `__ads__/` directory layout
- **5 Archive Formats** — ZIP, TAR+ZSTD, TAR+GZ, TAR+XZ, 7Z — all with full ADS support
- **SHA-256 Verification** — every stream hashed before packing; verified after extraction with `PRESERVED` / `MISSING` / `MISMATCHED` reporting
- **Forensic Manifest** — `manifest.json` embedded in every archive with file paths, stream names, sizes, and hashes
- **Operation Log** — timestamped plain-text log of every pack and extract operation
- **Stream Viewer** — inspect all ADS on any file before archiving
- **YARA Scanning** — rule-based malicious stream detection via yara-x
- **VirusTotal Lookup** — SHA-256 hash lookup via VirusTotal API
- **Live Progress** — real-time events streamed from Rust backend to frontend
- **Dark & Light Mode** — full theme support
- **Single `.exe`** — no installation required, no runtime dependencies (~5 MB vs ~150 MB for Electron)

### Python ADS Tool (`app.py`)
- Create, list, read, and delete ADS streams on any file, folder, or ZIP
- Direct Windows `kernel32.dll` calls via `ctypes` — same API as the Rust backend
- SHA-256 hash displayed immediately on every write
- Zero dependencies — Python stdlib only (`tkinter`, `ctypes`, `hashlib`, `threading`)
- Non-blocking — all operations run on background threads

---

## Archive Format

StreamSafe stores ADS inside standard archives using this layout:

```
archive.zip
├── manifest.json          ← forensic manifest with all hashes
├── operation.log          ← timestamped operation log
└── files/
    ├── document.txt       ← base file, byte-for-byte identical
    └── __ads__/document.txt/
        ├── Zone.Identifier  ← raw stream content, unmodified
        └── thumbnail        ← each stream stored separately
```

The `__ads__/` entries are standard files inside a standard archive — readable by any zip tool even without StreamSafe installed.

---

## Why This Matters

| Tool | ADS Preservation | SHA-256 Verify | Forensic Manifest | Open Source |
|------|-----------------|----------------|-------------------|-------------|
| 7-Zip | ❌ Silently drops | ❌ | ❌ | ✅ |
| WinRAR | ❌ Silently drops | ❌ | ❌ | ❌ |
| Windows ZIP | ❌ Silently drops | ❌ | ❌ | ✅ |
| FTK Imager | ✅ (E01 only) | ✅ | ✅ | ❌ Proprietary |
| **StreamSafe** | ✅ **Full** | ✅ | ✅ | ✅ **Apache 2.0** |

---

## Running the Python ADS Tool

```bash
python app.py
```

No `pip install` needed — zero third-party dependencies.

### Requirements

| Requirement | Detail |
|-------------|--------|
| Python | 3.8 or later |
| OS | Windows 10 / 11 only |
| File System | NTFS volume required |
| Dependencies | None — stdlib only |

All modules used (`tkinter`, `ctypes`, `hashlib`, `threading`, `os`, `sys`, `datetime`) are part of the Python standard library. The `requirements.txt` in this repository confirms this explicitly.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Desktop Framework | Tauri v2 |
| Backend | Rust (stable) |
| Frontend | React + TypeScript |
| Styling | Tailwind CSS |
| State | Zustand |
| Archives | zip · tar+zstd/gz/xz · sevenz-rust |
| Hashing | sha2 crate (SHA-256) |
| Windows APIs | windows crate (FindFirstStreamW, CreateFileW, …) |
| YARA | yara-x |
| Python GUI | tkinter (stdlib) |
| Python Win APIs | ctypes (stdlib) |

---

## Repository Structure

```
Bharat-Cares-by-SMEC-Trust-Bootcamp-with-IBM-Bootcamp/
├── app.py                                          ← Python ADS Tool (zero dependencies)
├── requirements.txt                                ← Confirms zero third-party dependencies
├── LICENSE.md                                      ← Apache 2.0
├── README.md
├── DevpalSinghCharanjeetSinghAnand_ProjectReport.html   ← Interactive project report
├── DevpalSinghCharanjeetSinghAnand_ProjectReport.docx   ← APA-formatted project report
│
├── IBM Certificate/
│   └── BharatCares.png                            ← IBM SkillsBuild completion certificate
│
├── Industry Connect Session/
│   └── 19th_October_2026.md                       ← Industry connect session notes
│
└── MasterClass Sessions/
    ├── 05th_October_2026.md
    ├── 07th_October_2026.md
    ├── 10th_October_2026.md
    ├── 14th_October_2026.md
    ├── 16th_October_2026.md
    └── 17th_October_2026.md
```

---

## Project Context

| Field | Detail |
|-------|--------|
| Programme | IBM SkillsBuild Cyber Security BootCamp 2026 |
| Organised by | BharatCares / Renalysis Consultants Pvt. Ltd. |
| Domain | Digital Forensics & File System Security |
| Author | Devpal Singh Charanjeet Singh Anand |

---

## License

This repository is licensed under the [Apache License 2.0](LICENSE.md).

Copyright 2026 Devpal Singh Charanjeet Singh Anand

---

*Learn. Build. Understand.*
