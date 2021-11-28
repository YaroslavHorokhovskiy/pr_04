"""Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується
з клавіатури (число непарне). У прикладі ширина дорівнює 5.
"""
max_width = int(input('Введіть ширину годинника (непарне число): '))

print()

# Верхня частина годинника
for width in range(max_width, 0, -2):
    space_width = (max_width - width) // 2 # Число пробілів ліворуч та праворуч
    print(' ' * space_width + '*' * width + ' ' * space_width)

# Нижня частина годинника
for width in range(3, max_width + 1, 2):
    space_width = (max_width - width) // 2
    print(' ' * space_width + '*' * width + ' ' * space_width)
