# Cybersecurity Bootcamp — Masterclass 3: Hacking 101

**Date:** 14th October 2026<br>
**Program:** IBM SkillsBuild Cybersecurity Bootcamp — BharatCares<br>
**Session:** Masterclass 3 — Hacking 101 (Ethical Hacking, Phishing & Live Demos)<br>
**Mode:** Live Interactive Session (Zoom + YouTube)<br>
**Host:** Vanita Tripathi | BharatCares<br>
**Guest Speaker:** Pranay Srivastava (Cybersecurity Professional — ex-external SOC team for Wells Fargo; worked in DRP — Digital Risk Protection)

---

## Session Overview

This was the third masterclass — a fast-paced, demo-heavy session by Pranay Srivastava. Where previous classes covered theory (CIA triad, social engineering types, OSINT tools), this session brought everything together with **live phishing page creation** (ZPhisher), **NMAP network scanning**, and a **full Metasploit exploit** against a Metasploitable VM.

Pranay also covered the Lockheed Martin Cyber Kill Chain, types of hackers, vulnerabilities, malware types, and finished with a thoughtful discussion on why cybersecurity matters beyond just "I have nothing to hide."

> *"Hacking is not always someone sitting in a dark room coding. It is a lot more than that — it is more of a mind game. Most of the time, the information is already available on the internet."*
> — Pranay Srivastava

---

## Pre-Session Announcements

| Item | Details |
|---|---|
| Learning Activity Deadline | Extended to **23rd October 2026** (festive season) |
| Project Submission Deadline | **23rd October 2026** |
| Attendance | Mandatory for all masterclasses |
| Next Masterclass | 16th October 2026 (Thursday), 5:00 PM – 7:00 PM |
| Resource Document | Contains all recordings, PPTs, query form, submission forms |

---

## Agenda

Pranay covered the following topics:

1. Hacking basics — what hacking really means
2. Ethical vs Malicious hacking
3. Types of hackers (White Hat, Black Hat, Grey Hat, Hacktivist, Script Kiddie)
4. **Cyber Kill Chain** — Lockheed Martin's 7-stage attack lifecycle
5. Vulnerabilities — system-based and human-based
6. Malware and ransomware types
7. Attack scenarios — Phishing, MITM, DDoS, Web attacks
8. **Live Demos:**
   - OSINT (Domain Dossier on IRCTC.com)
   - Phishing page creation with **ZPhisher**
   - URL shortening with TinyURL
   - **NMAP** network & OS scan
   - **Metasploit** exploit against Metasploitable VM

> ⚠️ *"These tools are strictly for educational purposes. The same tools are used by ethical and malicious hackers — the only difference is intent. Don't use them as pranks on your friends."*

---

## Why Cybersecurity Matters — Beyond "I Have Nothing to Hide"

Pranay addressed a common Indian mindset: *"Why would someone hack me? I have no data."*

### The WannaCry Hospital Scenario

When WannaCry ransomware hit, it attacked Delhi hospitals and others globally. Systems were encrypted — meaning doctors couldn't use computers, robotic surgery arms, or monitoring systems.

> *"Imagine somebody is lying on the operation table, all cut open, and at that moment the system stops working. It's not about money — it's about life and death."*

### The Broader Responsibility

- Your phone doesn't just contain **your** data — it contains contacts, photos, and chats of friends and family
- If your device is compromised through negligence, **others become vulnerable** to cyberbullying, blackmail, and fraud
- Cybersecurity is not about hiding things — it's about protecting the people who trust you

---

## CIA Triad — Quick Recap with Real-World Mapping

| Pillar | Meaning | Real-World Example (Payment Apps) |
|---|---|---|
| **Confidentiality** | Only authorised people access information | Only you can open your Google Pay / PhonePe / PayTM account |
| **Integrity** | Data stays accurate and unaltered | Your bank balance of ₹50,000 doesn't change because someone exploited a flaw |
| **Availability** | System is available when needed | If you're at a shop and the payment app's server is down, you can't pay the vendor |

> *"If even one pillar fails, the other two have no relevance. If confidentiality is gone, integrity and availability don't matter. They're interconnected."*

---

## Types of Hackers

| Type | Intent | Description |
|---|---|---|
| **White Hat** | Ethical, with permission | Penetration testers, vulnerability analysts — find flaws before attackers do |
| **Black Hat** | Malicious, criminal intent | Steal money, disrupt services, cause harm |
| **Grey Hat** | No permission, but doesn't exploit | Finds vulnerabilities and keeps them documented — sells to state-funded teams for use during wartime |
| **Hacktivist** | Political / ideological | Hacks government websites to make a point (e.g., Nepal/Bangladesh protests) |
| **Script Kiddie** | Copy-paste attacker | Uses pre-built tools without understanding them |

### Why White Hats Matter — Android Security Patches

> *"If you're using Android, in September or November, there's always a new security patch delivered. That's because white hats found bugs and patches were deployed."*

At the end of the day, **humans code the software** — and humans can't be 100% secure in their coding. That's why secure coding practices matter.

---

## Secure Coding — A Developer's Responsibility

> *"Secure coding means when a developer is coding, they must keep the security of the application in mind — not just randomly type and deploy."*

### Example: Plain Text Passwords

If a login form sends passwords as plain text over the network (not encrypted), anyone on the same network can intercept passwords using tools like Wireshark.

**Developers must:**
- Encrypt passwords in transit (HTTPS, TLS)
- Hash passwords at rest (bcrypt, argon2)
- Validate input (prevent SQL injection)
- Implement proper session management

---

## Cyber Kill Chain — Lockheed Martin's 7 Stages

| Stage | What Happens | Real-Life Thief Analogy |
|---|---|---|
| **1. Reconnaissance** | Gather info via LinkedIn, websites, DNS, leaked data | Walking around the house — observing who lives there, when they leave |
| **2. Weaponization** | Build the payload / malware / exploit | Preparing break-in tools |
| **3. Delivery** | Send the payload (phishing email, USB, etc.) | Approaching the house |
| **4. Exploit** | Trigger the vulnerability | Opening the door |
| **5. Installation** | Payload installs on the system | Getting inside |
| **6. Command & Control** | Attacker has remote control of the system | Searching through stuff inside the house |
| **7. Action on Objectives** | Steal data, encrypt files, etc. + **Clear tracks** | Rubbing doorknobs to remove fingerprints |

> 💡 **Key insight:** If you break ANY link in this chain, the attack fails. As a cybersecurity professional, your job is to identify at which stage you want to stop the attack.

---

## Live Demo 1 — OSINT with Domain Dossier

Pranay demonstrated how to gather publicly available information about any website using **Domain Dossier** (from the OSINT framework).

### Target: IRCTC.com

He entered IRCTC.com and selected:
- Domain WHOIS record
- DNS records
- Traceroute
- Network WHOIS
- Service scan

### What Was Revealed (All Public!)

| Info Type | What Was Found |
|---|---|
| Registrar | Public Domain Registry |
| Registrant Name | **Sanjay Agarwal** (real name exposed!) |
| Company Address | New World Enclave, Naroji Nagar, Sadarjung, New Delhi |
| Phone Number | Listed publicly |
| Abuse Email | Available for takedown requests |
| Network WHOIS | Hosting provider details |
| DNS Records | Mail servers, FTP, POP3, HTTP service status |

### How Attackers Use This

1. Find Sanjay Agarwal on LinkedIn
2. Discover he works in tech at IRCTC
3. Build a phishing email impersonating a friend/colleague
4. Send malware-laced attachment
5. If Sanjay clicks from his company laptop → lateral movement → access to IRCTC's systems

> *"This is how an attack happens. There's a lot that goes before the coding part — creating a persona, social engineering, targeting."*

---

## Live Demo 2 — Phishing Page with ZPhisher

> ⚠️ *"This is strictly for educational purposes. Don't use this on anyone — not even as a prank on friends."*

### What is ZPhisher?

ZPhisher is an open-source phishing page generator available on GitHub. It creates convincing login pages for:
- Facebook
- Instagram
- Google
- And 30+ other services

### Demo Steps

1. Open ZPhisher in Kali Linux terminal
2. Select target (e.g., Google)
3. Choose "New" version (more convincing)
4. Choose hosting option:
   - **Localhost** — only you can access (127.0.0.1)
   - **Cloudflare** — host on internet (requires Cloudflare token, paid)
   - **Local exposed** — accessible on local network

5. ZPhisher generates a fake Google login page
6. Victim enters credentials → clicks Sign In
7. Page redirects to **real** Google login (no suspicion raised)
8. **Attacker sees credentials in terminal!**

### URL Masking with TinyURL

Since phishing URLs are long and suspicious, attackers use **URL shorteners** like TinyURL:

```
Long URL → tinyurl.com/randomchars
```

> *"Seeing a long URL in a random mail makes people suspicious. But seeing a short URL, people don't mind — they just click."*

### Other Phishing Tools Mentioned

- **Camfish** — also creates phishing pages, gives exact GPS locations, asks for camera/location permissions

---

## Vulnerabilities, Threats, and Risks

### Vulnerability = Weakness / Loophole

| Common Vulnerability Types | Example |
|---|---|
| Unpatched software | Old Windows version with known CVEs |
| Weak/default credentials | admin/admin, password123 |
| Misconfigurations | Open ports that shouldn't be open |
| Injection flaws | SQL injection, command injection |
| Broken access control | User can access admin functions |
| **Human error** | The biggest vulnerability — always |

### How Many Ports Does a Device Have?

> **65,535 ports** — divided so different services can run on different ports.

#### Common Ports to Memorise (Interview Tip!)

| Port | Service |
|---|---|
| 20, 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 110 | POP3 |
| 143 | IMAP |
| 3306 | MySQL |
| 3389 | RDP |

> 💡 *"In entry-level interviews, they will 100% ask you — what port does HTTPS work on? What's on port 21? Memorise the basic 15-20 ports."*

---

## Malware Types

| Type | How It Spreads | What It Does |
|---|---|---|
| **Virus** | Attaches to files, **needs human interaction** | Replicates when file is opened |
| **Worm** | **Self-replicating**, no human interaction needed | Spreads across networks automatically |
| **Trojan** | Disguised as legit software | Hidden malware in movies, cracked software |
| **Botnet** | Network of compromised systems | Used in DDoS attacks |
| **Spyware / Keylogger** | Installed silently | Records every keystroke → sends to attacker |
| **Rootkit** | Embedded deep in OS | Hides from antivirus detection |

### Ransomware — A Life-and-Death Threat

WannaCry attacked Delhi hospitals, encrypting systems:
- Doctors couldn't access patient records
- Surgeries had to be postponed
- Robotic surgery arms stopped working mid-operation

> *"It's not just about money. It's about someone's life depending on that system."*

---

## Live Demo 3 — NMAP Network Scan

Pranay set up a virtual lab:
- **Attacker:** Kali Linux (IP: 192.168.1.110)
- **Target:** Metasploitable VM (IP: 192.168.1.111) — intentionally vulnerable machine

### NMAP OS Scan Command

```bash
nmap -O 192.168.1.1/24
```

This scans the entire subnet for:
- All connected devices (phones, smart TVs, laptops)
- Open ports on each device
- Operating system (with ~73% accuracy)
- MAC addresses (useful for MAC spoofing attacks)

### What NMAP Revealed

For Metasploitable, multiple ports were open:
- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 80 (HTTP)
- And many more...

> *"NMAP is one of the most used tools in cybersecurity. Even online, you'll find it at the top of every list."*

### Why We Need to Know the OS

Once you know the OS, you can:
1. Search for known vulnerabilities in that OS version
2. Find matching exploits in Metasploit
3. Launch targeted attacks

---

## Live Demo 4 — Metasploit Exploit

### What is Metasploitable?

> *"Metasploitable is a machine made with intent to be hacked. It has a lot of vulnerabilities built in — used for testing and learning."*

### Steps to Exploit FTP Service

1. Open Metasploit console: `msfconsole`
2. Search for FTP exploits: `search ftp`
3. Found two options:
   - DoS exploit (rank: normal)
   - **Backdoor command execution** (better for our purpose)
4. Get info about the exploit: `info <exploit_name>`
5. Use the exploit: `use <exploit_name>`
6. Set RHOST (target IP): `set RHOST 192.168.1.111`
7. Set LHOST (your IP): `set LHOST 192.168.1.110`
8. Run: `exploit`

### Result: Meterpreter Session Opened

Once exploited, Pranay had full access to the Metasploitable machine:

```bash
# Commands demonstrated:
sysinfo      # Shows OS, hostname, architecture
ls           # Lists files and directories
cd /dev      # Navigate to specific folder
whoami       # Shows current user
help         # Lists all meterpreter commands
```

### Available Meterpreter Commands

| Category | Commands |
|---|---|
| System | `cd`, `ls`, `pwd`, `cat`, `download`, `upload`, `rm`, `mkdir` |
| Webcam | `webcam_snap`, `webcam_stream` |
| Audio | `record_mic`, `webcam_chat` |
| Network | `portfwd`, `route`, `ipconfig` |
| Privilege escalation | `getsystem`, `hashdump` |

> *"Once you have a session, you can turn on the webcam, turn on the mic, copy files from his system to yours. That's how hacking is done."*

---

## Why You Shouldn't Use Public Wi-Fi

When you connect to public Wi-Fi:
1. Anyone on the same network can scan your device with NMAP
2. If your device has any unpatched vulnerability → exploited via Metasploit
3. Attacker gets full control (webcam, mic, files, passwords)

> *"That is why people recommend you don't use public Wi-Fi. Scan your home Wi-Fi with NMAP — see what devices are visible and what loopholes they have."*

---

## How to Set Up a Virtual Lab at Home

### Pranay's Recommended Approach (for Beginners)

1. Download **VMware Workstation** (or VirtualBox — free)
2. Go to **kali.org** → Get Kali → Download **pre-built VMware image** (NOT the ISO)
   - The ISO requires manual configuration — beginners get lost
   - Pre-built image is ready to use, no settings needed
3. Import the image into VMware
4. Download **Metasploitable** (intentionally vulnerable VM)
5. Connect both VMs to same NAT/host-only network
6. Start practicing with NMAP, Metasploit, ZPhisher

> *"Don't download the ISO — you'll get lost in configuration and your interest will be subdued. Use the pre-built image."*

---

## Key Q&A Highlights

| Question | Pranay's Answer |
|---|---|
| Why isn't India letting Starlink enter? | Security concerns — Starlink won't share user data with Indian government. Recent case: smugglers used Starlink, GOI asked for location data, Starlink denied citing privacy policy |
| Is it safe to open phishing link without giving permissions? | NO — clicking can trigger auto-download of malware. Even if the link asks for camera/location access (like Camfish), don't risk it. If it's fishy, don't click |
| How to start cybersecurity as a 1st year B.Tech student? | This bootcamp is a great start — you have reading material, masterclasses, demos. Start here, then explore TryHackMe, HackTheBox |
| Can ZPhisher run on Ubuntu? | Probably yes, not 100% sure — try it |
| Should we remember all NMAP commands? | Ideally yes, but practically impossible. Use them daily — gaps of 2-3 weeks lead to forgetting. Use `man`/help when needed |
| How to create a virtual lab? | Download VMware + pre-built Kali image + Metasploitable. Don't use ISO as beginner |

---

## Activity for Students

> *"Install Kali Linux at home. Scan your home Wi-Fi with NMAP. See how many devices are visible — phones, smart TVs, laptops. Try to find what loopholes they have. That's the activity for today and tomorrow."*

---

## Key Reminders

- 📅 **23rd October 2026** — Both learning activity AND project submission deadlines
- 💻 Install Kali Linux + Metasploitable at home and practice in a **safe lab environment**
- 🚫 Never use phishing tools on real people — even as pranks
- 🔒 Don't use public Wi-Fi for sensitive transactions
- 📚 Memorise basic ports (15-20) for interviews
- 🤝 Reach out to Pranay on LinkedIn for mentoring and doubt resolution

---

## Upcoming Session

| Detail | Info |
|---|---|
| Date | 16th October 2026 (Thursday) |
| Time | 5:00 PM – 7:00 PM |
| Session Type | Masterclass 4 — Future of Cybersecurity (AI threats & careers) |
| Trainer | Rushikesh Dinkar |
| Attendance | Mandatory — link shared on WhatsApp group & Zoom chat |
