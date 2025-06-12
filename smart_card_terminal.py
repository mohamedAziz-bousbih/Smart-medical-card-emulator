from pathlib import Path
import pickle
import datetime
from getpass import getpass
from card_emulator import VirtualCard
from utils.encrypt_utils import decrypt_json, encrypt_json

CARD_PATH = Path("data/virtual_card.bin")

ROLES = {
    "1": "Doctor",
    "2": "EMT",
    "3": "Pharmacist"
}

def verify_identity(role):
    if role == "1":
        name = input("Enter doctor name: ").strip()
        pin = getpass("Enter PIN: ")
        return name, pin if pin == "1234" else None

    elif role == "2":
        pin = getpass("Enter PIN: ")
        return "EMT", pin if pin == "1234" else None

    elif role == "3":
        name = input("Enter pharmacist name: ").strip()
        code = input("Enter pharmacy code: ")
        return name, code if code == "PHARMA42" else None

    return None, None

def show_menu():
    print("\nSelect an action:")
    print("[1] View patient info")
    print("[2] Add condition")
    print("[3] Add medication")
    print("[4] Add medical history")
    print("[5] View access log")
    print("[6] Exit")

def filter_data_by_role(data, role):
    if role == "Doctor":
        return data
    elif role == "EMT":
        return {k: data[k] for k in ["name", "blood_type", "allergies", "conditions", "emergency_contact"] if k in data}
    elif role == "Pharmacist":
        return {k: data[k] for k in ["name", "medications"] if k in data}
    return {}

def log_access(data, role, actor):
    entry = {
        "by": actor,
        "role": role,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    data.setdefault("access_log", []).append(entry)

def main():
    print("🟢 Smart Medical Card Scanner Ready")
    input("Insert card and press Enter...")

    if not CARD_PATH.exists():
        print("❌ No card detected.")
        return

    with open(CARD_PATH, "rb") as f:
        encrypted_data = pickle.load(f)

    card = VirtualCard()
    card.encrypted_data = encrypted_data

    print("\nSelect your role:")
    for k, v in ROLES.items():
        print(f"[{k}] {v}")
    role_key = input("Your role: ").strip()

    role = ROLES.get(role_key)
    if not role:
        print("❌ Invalid role.")
        return

    actor, verified = verify_identity(role_key)
    if not verified:
        print("❌ Authentication failed.")
        return

    print(f"✅ Access granted. Welcome, {actor} ({role})")

    try:
        patient_data = card.read("1234")  # static PIN unlock
        log_access(patient_data, role, actor)

        while True:
            show_menu()
            choice = input("Your choice: ").strip()

            if choice == "1":
                print("\n📋 Patient Info:")
                view_data = filter_data_by_role(patient_data, role)
                for k, v in view_data.items():
                    print(f"{k}: {v}")

            elif choice == "2":
                if role != "Doctor":
                    print("❌ Only doctors can add conditions.")
                    continue
                cond = input("Enter new condition: ").strip()
                patient_data.setdefault("conditions", []).append(cond)

            elif choice == "3":
                if role not in ["Doctor", "Pharmacist"]:
                    print("❌ Only doctors or pharmacists can add medications.")
                    continue
                name = input("Medication name: ").strip()
                dose = input("Dose: ").strip()
                freq = input("Frequency: ").strip()
                patient_data.setdefault("medications", []).append({
                    "name": name, "dose": dose, "frequency": freq
                })

            elif choice == "4":
                if role != "Doctor":
                    print("❌ Only doctors can add to medical history.")
                    continue
                diagnosis = input("Diagnosis: ").strip()
                date = input("Date (YYYY-MM-DD): ").strip()
                notes = input("Notes: ").strip()
                patient_data.setdefault("medical_history", []).append({
                    "diagnosis": diagnosis, "date": date, "notes": notes
                })

            elif choice == "5":
                if role != "Doctor":
                    print("❌ Access log is restricted to doctors.")
                    continue
                print("\n📜 Access Log:")
                for entry in patient_data.get("access_log", []):
                    print(f"{entry['timestamp']} - {entry['role']} - {entry['by']}")

            elif choice == "6":
                break

            else:
                print("❌ Invalid option.")

        # Encrypt and save updates
        card.write(patient_data)
        with open(CARD_PATH, "wb") as f:
            pickle.dump(card.encrypted_data, f)
        print("💾 Card updated and encrypted successfully.")

    except PermissionError:
        print("❌ Access denied. Invalid credentials.")

if __name__ == "__main__":
    main()
