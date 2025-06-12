import pickle
from card_emulator import VirtualCard
from pathlib import Path

# Simulate loading data from a real card
with open("data/virtual_card.bin", "rb") as f:
    encrypted_data = pickle.load(f)

card = VirtualCard()
card.encrypted_data = encrypted_data  # Restore the saved encrypted state

try:
    pin = input("Enter PIN to unlock card: ")
    data = card.read(pin)
    print("🔓 Decrypted data:", data)
except PermissionError:
    print("❌ Wrong PIN. Access denied.")

