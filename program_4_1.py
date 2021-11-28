"""Написати програму, яка зчитує 4 числа з клавіатури і виводить на екран
найбільше з них.
"""
numbers = []

for i in range(4):
    number = int(input(f'Введіть число #{i + 1}: '))
    numbers.append(number)

print(f'Найбільше число: {max(numbers)}')
