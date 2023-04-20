def p1():
    a = [10, 32, 45, 87, 99]
    b = int(input( "Введите число: "))
    if b in a:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def p2():
    a = [2, 15, 64, 15, 1, 2]
    print(*a)
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
          if a[i] == a[j]:
             print(a[i])


def p3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" )
    a = int(input("Введите количество выходных"))
    for i in week:
        print ("Ваши рабочие дни:", *week[:-a])
        print("Ваши выходные дни:", *week[-a:])
        break


def p4():
    import random
    a1 = ['Сухарев', 'Иванов', 'Нечаев', 'Соловьев', 'Жук', 'Шарин']
    a2 = ['Николаев', 'Пуджев', 'Пушкин', 'Волков', 'Воробьев', 'Лыткин']
    gutid = tuple(random.sample(a1,3) + random.sample(a2, 3))
    print("Группа1 :",*a1)
    print("Группа2 :",*a2)
    print("ГУТИД :",*gutid)
    print("Количество студентов в ГУТИД :",len(gutid))
    print(*sorted(list(gutid)))
    if 'Иванов' in gutid:
        print("Иванов входит в ГУТИД,", gutid.count('Иванов'))
    else:
        print("Иванов не спортсмен")
p1()
p2()
p3()
p4()