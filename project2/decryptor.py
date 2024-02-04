import os
from cryptography.fernet import Fernet

source_folder = "spy_reports"
folder2 = "decrypted_reports"

if not os.path.exists(folder2):
    os.makedirs(folder2)

key = "xb054FuBpfzYF5xvUYVjgWN9ln7dN91m2vHaEaFKUlM="
fernet_key = Fernet(key)

days = [f"{i:02d}_10_2023" for i in range(1, 32)]

for day in days:
    files_with_date = [filename for filename in os.listdir(source_folder) if day in filename]

    if files_with_date:
        print(f"Для {day} найден отчет: {', '.join(files_with_date)}")

        for filename in files_with_date:
            source_file_path = os.path.join(source_folder, filename)
            folder2_file_path = os.path.join(folder2, filename)

            with open(source_file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
                decrypted_data = fernet_key.decrypt(encrypted_data)

            with open(folder2_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)

            print(f"Отчет для {day} расшифрован и сохранен как {folder2_file_path}")

    else:
        print(f"Для {day} отчета нет")