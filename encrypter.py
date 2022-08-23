from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
import os


def encrypter_method(given_file_path, given_file_name, key):
    with open(given_file_path, "rb") as file2string:
        converted_string = base64.b64encode(file2string.read())
    data = converted_string
    file2string.close()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"AccSvd/{given_file_name}", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

    os.remove(given_file_path)
