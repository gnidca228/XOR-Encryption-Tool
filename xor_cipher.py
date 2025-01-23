class XORCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        encrypted_text = ""
        key_length = len(self.key)
        for i, char in enumerate(text):
            key_char = self.key[i % key_length]
            encrypted_text += chr(ord(char) ^ ord(key_char))
        return encrypted_text

    def decrypt(self, text):
        return self.encrypt(text)  # XOR encryption is symmetric