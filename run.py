import os
from tools import join_files, sort_files

# Папка где будут сохраняться файлы.
# directory = "C:\info\\"
directory = f"{os.getcwd()}\\info_about_machines\\"
nodes = ["v01", "v02", "v03", "v04"]
family = "family"
user = "user"
password = "password"


file = "main.bat"
if os.path.isdir(directory) is False:
    os.mkdir(directory)
with open(file) as file_in:
    text = file_in.read()
    text = text.replace("{DIRECTORY}", directory)
    text = text.replace("{USER}", user)
    text = text.replace("{FAMILY}", family)
    text = text.replace("{PASSWORD}", password)
    file_in.close()
for node in nodes:
    tmp_text = text.replace("{NODE}", node)
    with open("temp.bat", mode="w+") as file_out:
        file_out.write(tmp_text)
    file_out.close()
    print(f"Получаем данные с {node}")
    os.system("temp.bat")
    file_out.close()

#Перед запуском убедиться что указанная директория пуста.
sort_files.sorf_files(directory)
join_files.join_files(directory)
