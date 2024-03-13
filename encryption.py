import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path
from cryptography.fernet import Fernet
from random import SystemRandom
import os
import time

key = b''


def new_master_key(password_provided):
    global key
    password = password_provided.encode()  # Convert to type bytes
    cryptogen = SystemRandom()
    salt = cryptogen.randbytes(16)  # Generate a random salt

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Increase the length to 64 bytes
        salt=salt,
        iterations=100000,
        backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

    with open('key.key', 'wb') as file:
        file.write(key)
        file.close()

    print("Key has been saved", key)


def check_key():
    global key
    if path.isfile("key.key"):  # check if the key is existed

        file = open('key.key', 'rb')  # Open the file as wb to read bytes
        key = file.read()  # The key will be type bytes
        file.close()
        return True
    else:
        return False


def encrypting(message):
    global key
    message = message.encode()  # turn it to bytes

    f = Fernet(key)
    encrypted = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes
    encrypted = str(encrypted)
    return encrypted[1:len(encrypted)]


def decrypting(message):  # turn it to bytes
    global key
    try:
        encrypted = message.encode()

        f = Fernet(key)
        decrypted = f.decrypt(encrypted)  # Decrypt the bytes. The returning object is of type bytes
        print("Decrypting successfully \n\n")
        decrypted = str(decrypted)

        return decrypted[2:len(decrypted) - 1]
    except Exception:
        print("Invalid Key - Unsuccessfully decrypted")


if check_key():
    print("Your key has been successfully imported \n\n")
else:
    new_master_key("test")
