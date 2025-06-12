
# 🧠 Smart Medical Card Emulator

A simulation of a secure, portable, patient-owned medical smart card system — built to reflect how healthcare data could be decentralized, encrypted, and role-controlled.

---

## 🚀 Project Purpose

This emulator is the first step in a real-world infrastructure shift: giving patients total ownership of their medical data via encrypted smartcards. The emulator simulates:

- 🔐 AES-encrypted patient data stored on a smartcard (or `.bin` file for now)
- 🧠 Role-based access for Doctors, EMTs, and Pharmacists
- 🩺 Secure update of conditions, medications, and medical history
- 📜 Access logging per user + role
- 🔏 PIN or verification-protected access
- ⚙️ Modular, real-world-ready codebase for integration with NFC hardware

---

## 🗂 Project Structure

```
├── smart_card_terminal.py       # 🔁 Main entry point – simulates real card scanner
├── write_to_card.py             # 📝 Writes (or overwrites) encrypted patient file
├── read_from_card.py            # 🔓 Reads and decrypts card (debug use)
├── update_card.py               # 🧩 Append new medical data (simulated updates)
├── card_emulator.py             # 🔧 VirtualCard class for encrypt/decrypt
├── utils/
│   └── encrypt_utils.py         # 🔐 AES256 encryption & decryption logic
├── data/
│   ├── patient_sample.json      # 🧪 Base template patient file
│   └── virtual_card.bin         # 💾 Encrypted card data (simulated NFC card)
```

---

## 🧪 How to Use

### 🔨 1. Create an encrypted card:
```bash
python write_to_card.py
```

### 🧠 2. Run the main terminal simulation:
```bash
python smart_card_terminal.py
```

You will be prompted to:
- Insert card (simulated)
- Select your role (Doctor, EMT, Pharmacist)
- Verify your identity (PIN, code, etc.)
- Interact with the card based on your permissions:
    - View patient info
    - Add condition, medication, or history
    - View access logs (Doctor only)

### 📖 3. (Optional) View decrypted data:
```bash
python read_from_card.py
```

### ✍️ 4. (Optional) Update card without full scanner UI:
```bash
python update_card.py
```

---

## 🔒 Security Notes

- Data is encrypted using AES-256-GCM
- PIN-authentication currently simulated; biometric-ready architecture
- Full patient data never exists in plaintext outside runtime memory

---

## 💡 Vision

> We’re building the future of medical identity: encrypted, patient-owned, and portable.  
> Doctors should request access, not own your history.
> All of this will be linked to the future app/site that the user have access to his data. 
> Security measures Will dynamically adapted based on the access role and context, ensuring real-life alignment (e.g., emergency access vs. full clinical access).

---
### Role-Based Access Examples

| 👥 **Role / Scenario**         | 🔐 **Security Response**                                             |
|-------------------------------|----------------------------------------------------------------------|
| 👨‍⚕️ Doctor logs in            | Full patient data, audit log access — requires verified PIN          |
| 🚑 EMT scans during emergency | Limited access (allergies, blood type, conditions) — no PIN required |
| 💊 Pharmacist access          | Medications only — verified with pharmacy code                       |
| 🧬 Admin/family view *(future)*| View-only — QR token or fingerprint-based consent                    |


---

## ✅ Our Next Steps

- Integratation with actual NFC smartcards
- Adding fingerprint or biometric challenge
- Expand API layer to cloud-back sync 
- Add QR-based temporary unlock token for sharing

---

### Made with clarity, fire, and a refusal to repeat old systems.
