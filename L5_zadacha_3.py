"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

try:
    with open('file3.txt', 'r') as f:
        stroki = f.readlines()
        dohod_vseh = 0
        kol_sotrudnikov = 0
        print("Список сотрадников, чей оклад состаляет менее 20000 руб.:")
        for i in range(len(stroki)):
            slova = stroki[i].split() #Данные заведены в файл как в примере задачи
            familia = slova[0]
            oklad = float(slova[1])
            dohod_vseh += oklad
            kol_sotrudnikov += 1
            if oklad < 20000:
                print(familia)
        sr_dohod = round((dohod_vseh / kol_sotrudnikov), 2)
        print(f'Средняя величина дохода сотрудников: {sr_dohod}')
except IOError:
   print("Произошла ошибка ввода-вывода!")



