'''Вводятся три разных числа. Найти,
какое из них является средним (больше одного, но меньше другого).'''

print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())

if a < b < c or c < b < a:
    print('Среднее:', b)
elif b < a < c or c < a < b:
    print('Среднее:', a)
else:
    print('Среднее:', c)
