#первое задание
a = int(input("сколько тебе лет?"))
print("тебе", a, "лет")
#второе задание
a = int(input("первое число: "))
b = int(input("второе число: "))
print("их сумма: ", a + b)
#третье задание 
a = int(input("введите число и я скажу оно положительное или отрицательное"))
if a == 0:
    print("число 0 не положительное и не отрицательное")
elif a > 0:
    print("твое число положительное")
else:
    print("твое число отрицательное")
if a % 2 == 0:
    print("твое число четное")
else:
    print("твое число нечетное")
