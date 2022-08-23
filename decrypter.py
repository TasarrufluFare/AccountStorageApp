from Crypto.Cipher import AES
import base64
import os
from tkinter import messagebox


def decrypter_method(given_file_path, given_file_name, given_key):
    try:
        file_in = open(given_file_path, "rb")
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
        cipher = AES.new(given_key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        file_decrypted = open(given_file_path, 'w', encoding="UTF-8")
        file_decrypted.write(data.decode('UTF-8'))
        file_decrypted.close()

        file = open(given_file_path, 'rb')
        byte = file.read()
        file.close()

        new_db_file = given_file_name.split(".")
        new_db_file[-1] = "db"
        new_db_file_last_form = new_db_file[0]+"."+new_db_file[1]
        print("New db File last: "+new_db_file_last_form)


        # #if not os.path.exists(path_to_create):
        # file_count = 0
        # while os.path.exists(path_to_create):
        #     file_count = file_count + 1
        #     path_to_create = f"Operations/{file_name_origin}" + f" ({file_count})" + f"/Decrypted {file_name_origin}"

        #os.makedirs(path_to_create)
        decodeit = open(f"AccSvd/{new_db_file_last_form}", 'wb')
        decodeit.write(base64.b64decode(byte))
        decodeit.close()
        file_in.close()
        os.remove(given_file_path)

    except():
        messagebox.showinfo("Warning!", "Something went wrong.\nCheck your password file.")



