import base64, os
from . import ancrypt, utils


def decrypt(ciphertext:str):
    return ancrypt.load(ciphertext, text=True)

def encrypt(plaintext:str):
    _input = utils.carbon(plaintext)
    key = base64.b64encode(os.urandom(32)).decode()
    _input = utils.Encryption(key.encode(), text=True).write(key, _input)
    return _input
