from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

KEY = b'ThisIsA32ByteLongEncryptionKey!!'  # 32 bytes = AES-256


def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def encrypt_json(json_obj):
    raw = json.dumps(json_obj).encode()
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(raw))
    return {
        "ciphertext": base64.b64encode(ct_bytes).decode(),
        "iv": base64.b64encode(cipher.iv).decode()
    }

def decrypt_json(encrypted_obj):
    ct = base64.b64decode(encrypted_obj["ciphertext"])
    iv = base64.b64decode(encrypted_obj["iv"])
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct))
    return json.loads(pt.decode())
