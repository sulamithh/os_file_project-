from cryptography.fernet import Fernet
import os

folder_path = "decrypted_reports"

files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # print(content)

        prefix = content.replace("вра", "дру").replace("Вра", "Дру")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(prefix)
            file.write("\nПроверено!")
    else:
        print("Это папка")