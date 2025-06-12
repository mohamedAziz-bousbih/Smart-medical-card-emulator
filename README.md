# 🧠 Virtual Medical Smart Card Emulator

A simulated, encrypted smart medical card system — built for human data sovereignty.

This project emulates the behavior of a **MIFARE DESFire EV2-based smart card**, designed to securely store and manage a patient’s core medical identity: blood type, allergies, chronic conditions, medication, and more.

> ⚠️ This is a **virtual prototype** of an offline-first, cryptographically secure medical ID card. The physical version (using NFC smart cards + readers) will follow in the next stage.

---

## 🎯 Core Features

- 🔐 AES-encrypted patient data stored in memory
- 🔄 Simulates card read/write authentication flow
- 🔓 PIN-based access control
- 🧱 Designed to be portable to real hardware (e.g. DESFire EV2 + ACR122U reader)

---

## 🏗️ Project Structure

```bash
virtual_medcard/
├── card_emulator.py         # Virtual smart card logic
├── write_to_card.py         # Simulate writing encrypted data
├── read_from_card.py        # Simulate PIN + decrypt + read
├── utils/encrypt_utils.py   # AES encryption/decryption helpers
├── data/patient_sample.json # Demo patient record
├── LICENSE.txt              # Legal notice (custom license)
└── README.md                # You’re reading this
