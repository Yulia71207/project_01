# Задача 7
# Есть словарь кодов товаров



titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

#  Есть словарь списков словарей количества товаров на складе.

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}
 
# imya_tovara = 'Кроссовки тип 3 - Adidas'
# print('imya_tovara', imya_tovara)

# kod_tovara = titles [imya_tovara]
# print('kod_tovara', kod_tovara)

# spisok_skladov = sales [kod_tovara]
# print('spisok_skladov', spisok_skladov)

# sklad_0 = spisok_skladov[0]
# print('sklad_0', sklad_0)

# kolvo = sklad_0['quantity']
# print('kolvo', kolvo)

# cena = sklad_0 ['price']
# print('cena', cena)
# suma = kolvo * cena
# print( 'Сумма',suma)

name_tovara = list(titles)
print("Список товаров", name_tovara)
for name in name_tovara:
    imya_tovara = name
    print('imya_tovara', imya_tovara)

    kod_tovara = titles [imya_tovara]
    print('kod_tovara', kod_tovara)

    spisok_skladov = sales [kod_tovara]
    print('spisok_skladov', spisok_skladov)

    dlina = len(spisok_skladov)
    print("Длина списка складов", dlina)

    dlina_spisok = (list(range(0,dlina)))
    print("Превращаем длину списка складов в список",dlina_spisok)
    tovar_suma = 0
    tovar_kolvo = 0

    for nomer in dlina_spisok:
        print("Номер склада", nomer)

        sklad_0 = spisok_skladov[nomer]
        print('sklad_0', sklad_0)

        kolvo = sklad_0['quantity']
        print('kolvo', kolvo)

        tovar_kolvo = tovar_kolvo + kolvo
        print('Суммарное количество', tovar_kolvo)

        cena = sklad_0 ['price']
        print('cena', cena)
        suma = kolvo * cena
        print( 'Сумма',suma)
        tovar_suma = tovar_suma + suma
        print('Суммарная сумма', tovar_suma)
        print('\n')
    print(f"{name} - {tovar_kolvo} шт, стоимость {tovar_suma} руб")


# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
0 