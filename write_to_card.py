import json
import pickle
from card_emulator import VirtualCard
from pathlib import Path

with open(Path("data/patient_sample.json")) as f:
    patient = json.load(f)

card = VirtualCard()
card.write(patient)

# Save encrypted card data to file (simulating the card's memory)
with open("data/virtual_card.bin", "wb") as f:
    pickle.dump(card.encrypted_data, f)

print("✅ Encrypted data written to virtual card.")
