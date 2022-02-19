""" 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
list_firm = []
pribyl_vse = {}
sr_pribyl = {"average_profit": None}
try:
    with open("file7.txt", "rt") as f:
        lines = f.readlines()
        kol_firm = 0
        pribyl_bez_ubytkov = 0
        for line in lines:
            firmy = line.split()
            name_f = firmy[0]
            pribyl_f = int(firmy[2]) - int(firmy[3])
            pribyl_vse.update({name_f: pribyl_f})
            if pribyl_f > 0:
                kol_firm += 1
                pribyl_bez_ubytkov += pribyl_f
        sr_pribyl.update({"average_profit": round((pribyl_bez_ubytkov / kol_firm), 2)})
        list_firm.append(pribyl_vse)
        list_firm.append(sr_pribyl)
        print(list_firm)
        with open("file7.json", "w") as write_j:
            json.dump(list_firm, write_j)
except IOError:
    print("Произошла ошибка ввода-вывода!")