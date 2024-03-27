from cryptography.fernet import Fernet

def encrypt_message(key, message):
    """
    Encrypt a message using a key.
    """
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(key, encrypted_message):
    """
    Decrypt an encrypted message using a key.
    """
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message)
    return decrypted.decode()

key = Fernet.generate_key()
fernet = Fernet(key)
str = str(key)
print(str)
print(key)
print(type(key))
print(fernet)