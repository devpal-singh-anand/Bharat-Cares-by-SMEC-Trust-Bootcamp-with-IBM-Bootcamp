# Cybersecurity Bootcamp — Masterclass 2: Social Engineering, Phishing & OSINT

**Date:** 10th October 2026<br>
**Program:** IBM SkillsBuild Cybersecurity Bootcamp — BharatCares<br>
**Session:** Masterclass 2 — Social Engineering, Phishing Types & OSINT Tools<br>
**Mode:** Live Interactive Session (Zoom + YouTube)<br>
**Host:** Vanita Tripathi | BharatCares<br>
**Guest Speaker:** Anmol Madan (Cybersecurity Professional, BharatCares)

---

## Session Overview

This was the second masterclass — a fast-paced, hands-on session with Anmol Madan. The session was **highly interactive**, with the chat constantly buzzing with student answers, doubts, and reactions. Anmol didn't just lecture — he asked questions, ran live demos (Grabify link tracking, Epieos email lookup, HaveIBeenPwned breach check, PhishingBox IQ test), and ended with a strong note on cyber hygiene.

The session ran well over two hours and covered everything from the CIA triad to OSINT tools, social engineering attack types (phishing, vishing, smishing, whaling, spear phishing, tailgating, shoulder surfing), live URL-tracking demos, and password strength checks.

> *"This was the most interactive session so far. Students wanted more sessions like this where chat is open and we can communicate with the experts directly."*
> — Chat feedback from Chaudhary Parth

---

## Pre-Session Announcements (Vanita)

| Item | Details |
|---|---|
| WhatsApp Group | All resources, links, recordings shared here |
| Resource Document | https://docs.google.com/document/d/1vz0juOBeoKIAS7sF7-iuZynSfy1OYwTWHpst3MGQnoU/edit?usp=sharing |
| Learning Activity Deadline | 16th October 2026 |
| Next Session | 12th October 2026 — Doubt Solving Session |
| IBM SkillsBuild Registration | If "Sponsoring Organisation" doesn't show ACA BharatCares, reopen the official link |
| Certificate Submission | Google Form will be shared soon — submit final Cybersecurity Bootcamp certificate only |

---

## Quick Recap — CIA Triad

Anmol started by revisiting the three pillars from the previous masterclass:

| Pillar | Meaning | Example |
|---|---|---|
| **Confidentiality** | Information is secret — only authorised people can access it | Your password is private |
| **Integrity** | Information is accurate and not tampered with | Your marks aren't changed without permission |
| **Availability** | Information is accessible when needed | College result portal works on result day |

> *"Confidentiality = is it secret? Integrity = is it correct? Availability = is it accessible?"*

### Data vs Information

| Term | Meaning | Example |
|---|---|---|
| **Data** | Raw, unprocessed facts | `85, 90, 75` |
| **Information** | Processed, meaningful data | "A student's average mark is 83.3" |

---

## Cyber Hygiene

Just like personal hygiene protects you from germs, **cyber hygiene** protects you from digital threats.

### Cyber Hygiene Practices

- Use strong, unique passwords (mix of uppercase, lowercase, numbers, special characters)
- Enable MFA / 2FA
- Patch your OS regularly
- Use encryption where possible
- Don't share personal info on every site
- Don't spread your digital footprint unnecessarily

> *"Modassar Ali Khan: How to be safe from hackers (germs)?"*
> *"Anmol: Same as you'd protect yourself from germs — by maintaining hygiene."*

---

## Authentication Methods

Anmol asked the class what authentication methods they know. The chat exploded with answers:

| Method | Type |
|---|---|
| Password / PIN | Something you know |
| OTP (One Time Password) | Something you have |
| Passkeys | Cryptographic credential |
| TOTP (Time-based OTP) | App-generated code |
| Captcha | Completely Automated Public Turing test to tell Computers and Humans Apart |
| Biometric — fingerprint, face scan, iris scan, retina scan, voice recognition | Something you are |
| Smart cards, NFC, RFID cards, government IDs, membership cards | Something you have |
| Digital signature, electronic signature | Something you create |

> 💡 **Alan Turing** — Father of computer science. Cracked Nazi codes in WWII, laid foundation for modern computers and AI.

---

## Social Engineering — The Core Threat

> *"The first brain is the most vulnerable — because all data is stored there."*

Social engineering manipulates human psychology rather than hacking technology. Attackers exploit:

- **Fear** — "Your account will be blocked in 10 minutes"
- **Greed** — "You won ₹10,00,000, claim now"
- **Urgency** — "Complete your KYC immediately"
- **Curiosity** — "Click here to see who viewed your profile"
- **Authority** — Fake police officer, bank manager, IAS officer
- **Sympathy / Kindness** — "Friend in hospital, need money urgently"
- **Trust** — Pretending to be a friend, family member, or boss
- **Peer Pressure** — "Everyone is sharing this, you should too"

### Real Examples Shared by Students

- Digital arrest scam — fake police call threatening arrest
- Fake dating/relationship scams
- Lottery scams ("KBC lottery winner")
- Fake hospital emergencies for friends/family
- Big Billion Days phishing — "iPhone 18 at ₹6,000"
- Ransomware threats with morphed photos
- Fake internship/job selection emails

---

## Types of Phishing Attacks

| Type | Channel | Target | Example |
|---|---|---|---|
| **Phishing** | Email | Mass / general | Fake bank email with malicious link |
| **Vishing** | Voice call | Mass / specific | "I'm calling from SBI, share your OTP" |
| **Smishing** | SMS | Mass / specific | "Your parcel is pending, click this link" |
| **Spear Phishing** | Email/Msg | **One specific person** | Personalised email using your name, college, role |
| **Whaling** | Email | **High-profile targets** (CEO, govt, celebrity) | Fake email to CEO requesting urgent confidential payment |
| **Tailgating** | Physical | Authorised entry zones | Following employee through secure door without swiping card |
| **Shoulder Surfing** | Physical | Public spaces | Watching someone enter ATM PIN at a cash machine |

> 💡 **Phishing vs Spear Phishing vs Whaling** — Phishing sends the same bait to everyone. Spear phishing targets one specific person. Whaling targets "big fish" — high-profile individuals with deep pockets or strategic access.

### Tailgating vs Shoulder Surfing

| Aspect | Tailgating | Shoulder Surfing |
|---|---|---|
| What happens | Unauthorised person follows authorised person into restricted area | Attacker watches you type passwords/PINs from nearby |
| Where | Office entrances, secure zones | ATMs, public transport, cafés |
| Vector | Physical access breach | Visual observation |
| Similar concept | Piggybacking (when authorised person knowingly lets them in) | ATM camera spying, screen-peeking |

---

## Live Demo — URL Tracking with Grabify

Anmol demonstrated how attackers track victims through shortened URLs:

1. Attacker goes to **grabify.org**
2. Enters a legitimate-looking URL (e.g., instagram.com)
3. Grabify generates a **tracking link** (e.g., `https://urlto.me/261up`)
4. Victim clicks the link
5. Attacker sees victim's: **IP address, ISP, location (lat/long), device, browser, OS**

> ⚠️ *"My teacher says: Trust Nothing. Verify Everything. So I never open any link in my PC — I do it on my college and friend's PC."*
> — Dhruv Darji (chat)

### Browser Safety Discussion

| Browser | Verdict |
|---|---|
| Brave | Safe — built-in tracker blocking |
| Tor | Most anonymous — but be cautious on what you click |
| DuckDuckGo | Privacy-focused search engine |
| Incognito Mode | Does NOT hide your IP — only stops local history tracking |

---

## Live Demo — Email Lookup with Epieos

**Epieos.com** (and **BehindTheEmail.com**) — reverse lookup tools that show what's linked to an email address:

- Google account profile picture
- Calendar IDs (so you can see someone's day schedule)
- Linked social media accounts
- Phone numbers sometimes
- Passkeys

> ⚠️ These tools are **paid** (limited free searches). Better to use a temporary email (temp-mail) for OSINT research instead of your real email.

---

## Live Demo — HaveIBeenPwned

**HaveIBeenPwned.com** — checks if your email has been part of any known data breach.

Students reported their results in chat:
- Most: 0 breaches
- Some: 1 breach (common from Cutout.Pro and similar apps)
- A few: 3 breaches

> *"If you've used your email on many websites, but it shows 0 breaches, that means none of those sites were hacked yet. Change passwords regularly — and don't reuse."*

### What To Do If You're Pwned

1. Change the password on the breached account immediately
2. Change passwords on any other account using the same password
3. Enable MFA
4. Monitor for suspicious activity

---

## Password Strength Check — Bitwarden

**bitwarden.com/password-strength** — checks how long it would take to crack your password.

> ⚠️ Don't enter your actual password! Use a similar-pattern password to test strength.

A strong password like `@     @ @ @ @ @.      .` (random mix of special chars) takes years to crack. A weak password like `password123` cracks in milliseconds.

---

## Live Demo — Phishing IQ Test

**phishingbox.com/phishing-iq-test/quiz.php** — shows you 10 emails and asks you to identify which are phishing vs legitimate.

Student results:
| Score Range | Number of Students (approx) |
|---|---|
| 10/10 | 5+ students |
| 9/10 | 8+ students |
| 8/10 | Many |
| 6-7/10 | Several |
| Below 6 | A few |

> *"All hyphenated ones (websites with `-`) were phishing. I got 8/10."*
> — Daksh Rathi

### How to Spot a Phishing Website

| Signal | Suspicious If... |
|---|---|
| URL | Uses hyphens, misspelled brand names (e.g., `paytm-offers.com`) |
| HTTP vs HTTPS | HTTPS doesn't guarantee safety — but HTTP is always suspicious |
| Sender email | Doesn't match the domain |
| Urgency | "Account blocked in 10 minutes", "limited offer expires tonight" |
| Generic greeting | "Dear Customer" instead of your name |
| Request for OTP/password | Legitimate services never ask for these |

> 💡 HTTPS doesn't mean safe — scammers can buy legitimate HTTPS certificates. But HTTP almost always = danger.

---

## Tools & Resources Shared in Session

| Tool | URL | Purpose |
|---|---|---|
| Grabify | grabify.org | URL tracking, IP grabber |
| Epieos | epieos.com | Email reverse lookup |
| BehindTheEmail | behindtheemail.com | Email info lookup |
| HaveIBeenPwned | haveibeenpwned.com | Check if email is in known breaches |
| Bitwarden Strength | bitwarden.com/password-strength | Test password strength |
| PhishingBox IQ Test | phishingbox.com/phishing-iq-test/quiz.php | Practice spotting phishing emails |
| Rakshagrid Digital | rakshagrid.com | Free OSINT tool (mentioned by student) |

---

## Cyber Helpline Numbers

| Number | Purpose |
|---|---|
| 1930 | National Cyber Crime Helpline (India) |
| 1091 | Women's helpline |

> ⚠️ Students reported mixed experiences — calls sometimes go unanswered. Persistence is key. File FIRs for serious cases.

---

## Key Q&A Highlights

| Question | Answer |
|---|---|
| How to know if a website is authentic? | Check HTTPS, verify domain spelling, look for reviews, check trust seals |
| Is Brave browser safer than Chrome? | Yes — built-in tracker blocking |
| What is Wireshark? | Network traffic capturing tool — used to analyse packets on any website |
| Is Tor legal in India? | Using Tor itself is legal — but illegal activities on it are not |
| My email has 1 breach — what to do? | Change password immediately, enable MFA, check other accounts using same password |
| Will today's recording be shared? | Yes — via WhatsApp group & resource document |
| Can someone access my phone camera? | Yes — if you've installed a malicious app. Check app permissions regularly |
| When is the next class? | 12th October — Doubt Solving Session |

---

## Session Feedback (From Chat)

> *"Anmol sir is best. Today we enjoyed so much."* — Adarsh Trivedi
> *"Energetic session today Anmol Sir."* — Ajinkya Sonawane
> *"Great session, need more. Bring full month series."* — Rahul Melkani
> *"Yes ma'am we want this type of interactive sessions where chats are not restricted."* — Chaudhary Parth

---

## Key Reminders

- 📅 Complete IBM SkillsBuild learning activity by **16th October 2026**
- 🛡️ Change passwords if you have any breaches (check HaveIBeenPwned)
- 🔐 Enable MFA on all critical accounts today
- 📂 All session recordings, PPTs, and links shared via WhatsApp group & resource document
- 💡 Take the PhishingBox IQ test — practice makes you safer
- 🤝 Connect with Anmol Madan on LinkedIn: **linkedin.com/in/anmolmadan7/**

---

## Upcoming Session

| Detail | Info |
|---|---|
| Date | 12th October 2026 (Monday) |
| Time | 5:00 PM |
| Session Type | Doubt Solving Session |
| Purpose | Resolve all your doubts about registration, certificates, project, Kali Linux |
| Attendance | Not mandatory today (per Vanita) — but mandatory for next masterclass |
