"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

try:
    with open('file2.txt', 'rt') as f:
        stroki = f.readlines()
        print(f'Всего в файле строк: {len(stroki)}')
        for i in range(len(stroki)):
            slova = stroki[i].split()
            print(f'В строке {i + 1} слов: {len(slova)}')
except IOError:
   print("Произошла ошибка ввода-вывода!")


