"""Обчислити за допомогою циклу факторіал числа n.
"""
number = int(input('Введіть будь-яке ціле позитивне число: '))

factorial = 1

for i in range(number, 1, -1):
    factorial *= i

print(f'Факторіал числа: {factorial}')
