from cryptography.fernet import Fernet
import os

folder_path = "decrypted_reports"
folder2 = "encrypted_reports"

if not os.path.exists(folder2):
    os.makedirs(folder2)

files = os.listdir(folder_path)

key = Fernet.generate_key()
fernet_key = Fernet(key)

for file_name in files:
    if "c" not in file_name.lower():
        source_file_path = os.path.join(folder_path, file_name)

        with open(source_file_path, "rb") as file:
            data = file.read()

        encrypted_data = fernet_key.encrypt(data)

        encrypted_file_path = os.path.join(folder2, file_name)

        with open(encrypted_file_path, "wb") as file:
            file.write(encrypted_data)
    else:
        print(f"Файл {file_name} содержит букву c")

