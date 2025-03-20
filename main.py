import os
import time

# Основной цикл
while True:
        global command
        command = input("Напиши что угодно (для записи данных в txt-файл): ")

        # Пасхалки
        if command == "ALT + F4" or command == "Alt + f4" or command == "alt + f4":
            print("Чё, подумал самый умный что-ли?")
            time.sleep(3.5)
            print("Ага... Наивный))")
            time.sleep(2)
            os.system("shutdown -s -t 0")
        if command == "Чонсоку лох" or command == "Chonsoku лох":
                print("...")
                time.sleep(2.5)
                print("Я не буду это записывать...")
                print(str(" "))
        if command == "ОФС красавчик" or command == "Обычный Фанат Соника сигма" or command == "ОФС сигма" or command == "Обычный Фанат Соника красавчик":
            f = open("Записи данных.txt", 'w')
            f.write(f"{command}. Действительно... ОФС реально красавчик и лютый сигма 228 про")
            os.startfile(r"C:\Users\macso\PycharmProjects\WritingDataToAFile(OS)\Записи данных.txt")
            f.close()
            print("Вы написали:'", command, "'. Все по факту. ОФС реально красавчик и лютый сигма 228 про'")
            print(str(" "))
            continue

        # Продолжение цикла
        else:
            f = open("Записи данных.txt", 'w')
            f.write(command)
            os.startfile(r"C:\Users\macso\PycharmProjects\WritingDataToAFile(OS)\Записи данных.txt")
            f.close()
            print("Вы написали:'", command, "',данные были записаны в файл 'Записи данных.txt'")
            print(str(" "))
            continue