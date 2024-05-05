num1 = int(input('Введите первое число: '))
if num1 >= 3 and num1 <= 20:
    parole_ = []
    for i in range(1, num1-1):
        for j in range(i+1, num1):
            var_ = i +j
            if num1 % var_ == 0 and i != j:
                twin = [i, j]
                parole_.append(twin)

    print("Первое число: ", num1, ' ', "Пароль: ", parole_)
else:
    print("Ошибка. Введено число не из требуемого диапазона")


