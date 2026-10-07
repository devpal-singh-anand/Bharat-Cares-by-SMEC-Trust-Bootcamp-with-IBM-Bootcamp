# Cybersecurity Bootcamp — Masterclass 1: Cybersecurity Fundamentals

**Date:** 07th October 2026<br>
**Program:** IBM SkillsBuild Cybersecurity Bootcamp — BharatCares<br>
**Session:** Masterclass 1 — Cybersecurity Fundamentals<br>
**Mode:** Live Interactive Session (Zoom + YouTube)<br>
**Host:** Vanita Tripathi | BharatCares<br>
**Guest Speaker:** Ayush Kumar (AI & Cybersecurity Expert, Corporate Trainer — worked with IBM, Microsoft, Delhi Police Cybercell)

---

## Session Overview

This was the first masterclass of the two-week bootcamp, conducted by Ayush Kumar. It was an interactive, ground-up session covering the fundamentals of cybersecurity — from the CIA triad to live demonstrations of Kali Linux tools like Hydra, Burp Suite, and Wireshark.

The session had a brief connectivity disruption mid-way due to bad weather, but Ayush rejoined and continued. Vanita also walked students through the IBM SkillsBuild registration steps, certificate download process, and answered dozens of student queries at the end.

> *"Cybersecurity is something which affects every single person who uses a smartphone, Instagram, Gmail, WhatsApp, UPI, and any app connected to the internet. Whether you are a B.Tech, BCA, BVA, MBA, or any other background — this session is for you."*
> — Ayush Kumar

---

## Pre-Session Announcements (Vanita)

| Item | Details |
|---|---|
| Attendance | Mandatory for all masterclasses — form shared at end of every session |
| Learning Activity Deadline | 16th October 2026 (4 modules, ~10 hours total) |
| Next Masterclass | 10th October 2026 (Saturday), 5:00 PM – 7:00 PM |
| WhatsApp Group | All resources, links, and updates shared here |
| Missed Class Policy | If you miss a class due to emergency, send a mail explaining the reason |
| Resource Document | Contains video tutorials, step-by-step guides, PPTs |
| Query Form | Shared at end of session for any doubts |

---

## Recap: IBM SkillsBuild Registration

Vanita quickly walked through the registration steps again for late joiners:

1. Scan the QR code or open the shared IBM SkillsBuild link
2. Click **Sign Up with Google** → choose your Google account → Continue
3. Select Country → India → Continue
4. Fill profile details — ⚠️ **enter your name carefully**, it appears on certificates
5. Confirm Sponsoring Organisation is **ACA BharatCares**
6. Skip Additional Information (optional)
7. Accept Terms & Conditions → Submit
8. Click **Go to SkillsBuild** → Enroll in **Cybersecurity Bootcamp**
9. Begin with Module 1 → Click **Go to Activity**

> ⚠️ If you see a multi-factor authentication page — select your email, input the OTP received, and click Verify.

### Certificate Download

- Complete each module 100% (read content, watch videos, attempt quizzes)
- Go back one step → **Actions** column → **View Completion Certificate**
- Download PDF or take screenshot
- You will get 4 individual certificates + 1 final Cybersecurity Bootcamp certificate (only after all 4 modules are done)

> *"The final Cybersecurity Bootcamp certificate is what you submit to us. You'll get it only after completing all four modules."*
> — Vanita Tripathi

---

## Session Agenda — What Was Covered

Ayush structured the session around 8 major sections:

1. What is Cybersecurity?
2. Common Cyber Threats
3. Passwords & MFA
4. Think Like an Attacker (attacker lifecycle)
5. Kali Linux Tools & Applications (live demo)
6. Digital Safety Habits
7. Interactive Q&A
8. Wrap-up

---

## What is Cybersecurity?

> *"Hacking is related to cybersecurity, but cybersecurity is much bigger than hacking."*
> — Ayush Kumar

Cybersecurity is about **protecting what matters in the digital world** — your personal data, digital identity, smartphone, laptop, network, and applications.

### The 3 Pillars — CIA Triad

| Pillar | Meaning | Real-World Example |
|---|---|---|
| **Confidentiality** | Only authorised people should access your information | Your Instagram password is known only to you |
| **Integrity** | Information should remain accurate and unaltered | If bank balance is ₹50,000, no one can change it without authorisation |
| **Availability** | Information and systems should be available when needed | WhatsApp lets you scroll back to last week's chats anytime |

> WhatsApp, Instagram, Facebook — all align with the CIA triad. Confidentiality = no one else logs into your account. Integrity = messages aren't tampered in transit. Availability = your old chats are always retrievable.

---

## Common Cyber Threats

### 1. Phishing
Attackers trick you into revealing sensitive information or clicking malicious links.

**Example:** You receive a message — *"Your SBI account will be blocked today. Click here to verify."*
Most people click immediately without checking the sender. That's phishing.

> *"Before clicking any mail or link, think — who is the sender? Check the sender's IP. Then you can click."*

### 2. Password Attack
If your password is `123456`, `password123`, or `yourname@123` — it can be cracked in seconds. Tools like **Hydra** can brute-force weak passwords using dictionary attacks.

### 3. Malware
Malicious software designed to harm, spy, steal data, or gain unauthorised access. A malicious PDF attachment can crash your system the moment you open it.

### 4. Ransomware
Imagine all your files suddenly become inaccessible, and you see a message asking for money. The infamous 2017 WannaCry attack encrypted company data globally and demanded ransom for decryption.

### 5. Web Application Attack
Vulnerabilities (loopholes/weaknesses) in poorly secured websites can be exploited. Ayush shared that he himself had tested his own college website and found multiple vulnerabilities — most college websites have them.

### 6. Social Engineering
Instead of attacking the computer, attackers attack **you** — manipulating the human being.

> *"Someone calls and says: 'Hello sir, I'm calling from your bank, please share your OTP for verification.' Many people share their OTP. The technology isn't being attacked — the human is being manipulated."*

### 7. MITM (Man-in-the-Middle)
Attacker positions themselves between you and the website you're communicating with — intercepting and altering data in transit.

### 8. DoS / DDoS (Denial of Service)
Server gets flooded with too many requests at the same time, causing it to crash. That's why college portals often go down during exam-result season.

---

## Passwords & MFA

### Strong Password Habits

- **Don't** use `123456`, `password123`, your date of birth, or your friend's name
- **Don't** use the same password across multiple accounts — if one leaks, all are vulnerable
- **Do** use different passwords for different accounts
- **Do** make passwords long, with mix of uppercase, lowercase, numbers, and special characters

### Multi-Factor Authentication (MFA)

> *"MFA is my favourite security habit personally."*
> — Ayush Kumar

MFA = don't rely only on a password. Three factors:

| Factor Type | Example |
|---|---|
| Something you **know** | Password |
| Something you **have** | Phone, security key |
| Something you **are** | Fingerprint, face scan |

Even if an attacker gets your password, they're stopped by the second factor.

> *"If you haven't enabled MFA on Gmail or Instagram yet, today is the day you secure your accounts."*

---

## Think Like an Attacker — Attacker Lifecycle

> *"Think like an attacker — not so that you become one, but so that you understand how to defend against one."*

If Ayush gave you a website (e.g., `gurugramuniversity.com`), what would an attacker try to find?

1. **Reconnaissance** — IP address, technologies used, subdomains, login pages, employee emails
2. **Scanning** — open ports, services running on the system
3. **Enumeration** — deeper info: name, DOB, email, phone number
4. **Exploitation** — take advantage of discovered vulnerabilities
5. **Privilege Escalation** — if limited access is gained, try to obtain higher privileges
6. **Maintain Access**
7. **Defender identifies & responds**

---

## Kali Linux Tools — Live Demo

> *"Kali Linux is not a hacking button. It's a toolbox — like a mechanic's toolbox with screwdrivers, hammers, and other tools. You need knowledge, skill, and ethical authorisation."*
> — Ayush Kumar

### How to Install Kali Linux

1. Visit **kali.org**
2. Click **Get Kali**
3. Download two things:
   - **Installer Image** (~4.4 GB)
   - **Pre-built VMware** (~3.6 GB)
4. Install **VMware Workstation** on your laptop
5. Set up the Kali Linux environment inside VMware

> ⚠️ Ayush expects all students to have Kali Linux installed before the next class — upcoming sessions will include hands-on practicals.

### Tools Demonstrated / Mentioned

| Tool | Purpose |
|---|---|
| **NMAP** | Network scanning, find open ports & services |
| **Metasploit** | Exploit framework for vulnerabilities |
| **Hydra** | Password cracking via dictionary/brute-force attacks |
| **Burp Suite** | Web application vulnerability scanner (intercept requests, sniper/battering attacks) |
| **Wireshark** | Packet analyser — capture data sent between devices |
| **Kismet** | Wireless network detector |

### Useful Commands in Kali Linux Terminal

| Command | Purpose |
|---|---|
| `whoami` | Shows current user (e.g., `kali2020`) |
| `ip a` (or `ifconfig`) | Find your system's IP address |
| `ping <IP>` | Check if a system is reachable (e.g., `ping 127.0.0.1`) |

### Hydra — Password Cracking Demo

1. Enter target IP address
2. Select port and service
3. Provide username (or upload a user list)
4. Upload a dictionary file (combinations of passwords)
5. Configure number of tasks, timeout
6. Start → Hydra tries each password combination until one works

> *"With a good dictionary, you can potentially crack someone's Instagram password. That's why strong passwords matter."*

---

## Digital Safety Habits — Checklist

- ✅ Use strong, unique passwords for every account
- ✅ Enable MFA wherever available
- ✅ Be careful with links and attachments — verify sender first
- ✅ Keep your devices updated
- ✅ Be aware of phishing attempts — check for fake URLs, urgency cues
- ✅ Share sensitive info only with trusted sources
- ✅ Use secure Wi-Fi networks
- ✅ **Think before you share**

---

## How to Start a Career in Cybersecurity

> *"Don't start by trying to hack Instagram or someone's Wi-Fi. Start with the fundamentals — networking, Linux, and Python. These are the pillars."*
> — Ayush Kumar

- Learn networking basics
- Get comfortable with Linux (Kali Linux as a starting point)
- Learn Python scripting
- Understand how technology can fail
- Study how attackers think
- Build systems that secure networks

> *"Don't become someone who knows how to hack. Become someone who knows how to secure."*

---

## Key Q&A Highlights

| Question | Ayush's Answer |
|---|---|
| Can I install Kali Linux on Windows? | Yes — install VMware Workstation on Windows, then set up Kali inside it |
| I don't have a laptop — what do I do? | Go to a nearby cyber café to practice. Theory alone won't teach cybersecurity |
| If an attacker steals password + OTP via SIM swap, is MFA still effective? | Cut off internet, change passwords immediately, then investigate further |
| Which installer to download — weekly or net installer? | Install the Kali ISO file + VMware Workstation (both required) |
| Will I learn Kali Linux in upcoming classes? | Yes — install it before next class so you can follow along practically |
| Will the recording be shared? | Yes — recordings of all masterclasses will be shared via the resource document |

---

## Key Reminders

- 📅 Complete the IBM SkillsBuild learning activity by **16th October 2026**
- 💻 Install Kali Linux + VMware **before the next masterclass** — practicals start next session
- 📝 Mark attendance for today's class — link shared in chat & WhatsApp
- 📂 All PPTs, recordings, and step-by-step guides are in the **resource document** on WhatsApp
- 🛡️ Enable MFA on your Gmail, Instagram, and bank accounts today
- 🤝 Connect with Ayush Kumar on LinkedIn for further guidance (QR was shared in session)

---

## Upcoming Session

| Detail | Info |
|---|---|
| Date | 10th October 2026 (Saturday) |
| Time | 5:00 PM – 7:00 PM |
| Session Type | Masterclass 2 — Phishing, Social Engineering & Tools |
| Attendance | Mandatory — link shared on WhatsApp group & Zoom chat |
