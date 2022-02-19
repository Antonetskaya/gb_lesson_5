"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

try:
    with open("file4.txt", "rt") as f:
        chisla_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        lines = f.readlines()
        for line in range(len(lines)):
            el = lines[line].split()
            slovo_eng = el[0]
            slovo_rus = chisla_dict.get(slovo_eng, 0)
            with open("file4_1.txt", "a") as f:
                print(f'{slovo_rus} {el[1]} {el[2]}', file=f)
            print(slovo_rus) #для проверки вывода
except IOError:
    print("Произошла ошибка ввода-вывода!")




