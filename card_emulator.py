from utils.encrypt_utils import encrypt_json, decrypt_json

class VirtualCard:
    def __init__(self):
        self.encrypted_data = None
        self.pin = "1234"

    def write(self, json_data):
        self.encrypted_data = encrypt_json(json_data)

    def read(self, pin_attempt):
        if pin_attempt != self.pin:
            raise PermissionError("Invalid PIN")
        return decrypt_json(self.encrypted_data)
