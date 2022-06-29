import json
print("Здравстуйте")
lang = ["русский", "казахский", "английский"]
rezhim = input("Выберете режим: 1-шифровка шифр цезаря, 2-расшифровка шифр цезаря, 3-добавить язык, 4-удалить язык, 5-напечатать все языки, 6-шифр перестановка расшифровка, 7-шифр перестановка шифровка, стоп-выход")
with open("alfabets.json", "r", encoding = "utf-8") as f:
    alfabets = json.load(f)

while rezhim != "стоп":
    if rezhim == "1":
        print("Выберите язык:", lang)
        alfabet = input()
        num = int(input("Ключ(любое число)"))
        print("Слово на языке", alfabet, "(без заглавных букв, пробелов, символов)")
        str_ = input()
        print("Слово зашифровано:")
        str2 = ""
        for i in str_:
            # if alfabets[alfabet].find(i) + num > len(str(alfabets[alfabet])):
                # while alfabets[alfabet].find(i) + num > len(str(alfabets[alfabet])):
                    # flag = num
                    # num = alfabets[alfabet].find(i) + num - len(str(alfabets[alfabet])) - 1
                    # str2 += alfabets[alfabet][alfabets[alfabet].find(0) + num]
                    # num = flag
            # else:
                # str2 += alfabets[alfabet][alfabets[alfabet].find(i) + num]
            str2 += alfabets[alfabet][(alfabets[alfabet].find(i) + num) % len(alfabets[alfabet])]
        print(str2)
    elif rezhim == "2":
        print("Выберите язык:", lang)
        alfabet = input()
        num = int(input("Ключ(любое число):"))
        print("Слово зашифрованое шифром Цезаря на языке", alfabet, "(без заглавных букв, пробелов, символов):")
        str_ = input()
        print("Слово зашифровано:")
        str2 = ""
        for i in str_:
            str2 += alfabets[alfabet][alfabets[alfabet].find(i) - num]
        print(str2)
    elif rezhim == "3":
        print("Какой язык хотоите добавить (", lang, "):")
        alfabet = input("")
        lang.append(alfabet)
        alfabets[alfabet] = input("Напишите алфавит этого языка(без пробелов, заглавных букв):")
        print('Язык добавлен:', lang)
    elif rezhim == "4":
        print("Какой язык хотоите удалить (", lang, "):")
        alfabet = input()
        del alfabets[alfabet]
        print('Язык удалён:', lang)
    elif rezhim == "5":
        print("Все языки:", alfabets)
    elif rezhim == "6":
        key1 = input("Введите ключ номер 1(Например: 1-а 2-б;через пробел):").split()
        key2 = input("Введите ключ номер 2(Например: 12345):")
        str_ = ""
        for i in range(len(key2)):
            for e in range(len(key1)):
                if key2[i] == key1[e][0]:
                    str_ += key1[e][2]
        print("Слово расшифровано:", str_)
    elif rezhim == "7":
        key1 = input("Введите ключ номер(Например: 1-а 2-б;через пробел):").split()
        key2 = input("Введите слово(Например: абвгд):")
        str_ = ""
        for i in range(len(key2)):
            for e in range(len(key1)):
                if key2[i] == key1[e][2]:
                    str_ += key1[e][0]
        print("Слово расшифровано:", str_)
    rezhim = input("Выберете режим: 1-шифровка шифр цезаря, 2-расшифровка шифр цезаря, 3-добавить язык, 4-удалить язык, 5-напечатать все языки, 6-шифр перестановка расшифровка, 7-шифр перестановка шифровка, стоп-выход")

with open('alfabets.json', 'w', encoding = "utf-8") as f:
    f.write(json.dumps(alfabets))

print("До свидания")