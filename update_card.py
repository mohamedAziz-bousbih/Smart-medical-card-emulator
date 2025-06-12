from pathlib import Path
import pickle
from card_emulator import VirtualCard
from utils.encrypt_utils import decrypt_json, encrypt_json


card_path = Path("data/virtual_card.bin")

if not card_path.exists():
    print("❌ No virtual card found. Run write_to_card.py first.")
    exit()

# Load encrypted card
with open(card_path, "rb") as f:
    encrypted_data = pickle.load(f)

card = VirtualCard()
card.encrypted_data = encrypted_data

try:
    pin = input("Enter PIN to unlock card: ")
    patient_data = card.read(pin)

    print("What do you want to add?")
    print("[1] Medical condition")
    print("[2] Medication")
    print("[3] Medical history entry")
    choice = input("Your choice: ")

    if choice == "1":
        new_condition = input("Enter new condition: ").strip()
        patient_data.setdefault("conditions", []).append(new_condition)

    elif choice == "2":
        med_name = input("Medication name: ")
        dose = input("Dose (e.g. 20mg): ")
        frequency = input("Frequency (e.g. Once daily): ")
        new_med = {
            "name": med_name,
            "dose": dose,
            "frequency": frequency
        }
        patient_data.setdefault("medications", []).append(new_med)

    elif choice == "3":
        diagnosis = input("Diagnosis: ")
        date = input("Date (YYYY-MM-DD): ")
        notes = input("Notes: ")
        history_item = {
            "diagnosis": diagnosis,
            "date": date,
            "notes": notes
        }
        patient_data.setdefault("medical_history", []).append(history_item)
    else:
        print("❌ Invalid option.")
        exit()

    # Encrypt and save updated card
    card.write(patient_data)
    with open(card_path, "wb") as f:
        pickle.dump(card.encrypted_data, f)

    print("✅ Updated successfully. Card re-encrypted.")

except PermissionError:
    print("❌ Wrong PIN. Access denied.")
