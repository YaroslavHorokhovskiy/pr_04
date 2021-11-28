"""За допомогою циклів вивести на екран всі прості числа від 1 до 100.
"""
print('Прості числа від 1 до 100:')

for i in range(2, 100): # Прості числа починаються з 2
    prime_number = True

    for j in range(2, i):
        # Просте число має ділитися без залишку лише на себе та на одиницю
        if i % j == 0:
            prime_number = False
            break

    if prime_number:
        print(i, end=' ')

print()
