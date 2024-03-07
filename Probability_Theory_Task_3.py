"""
Задача:
3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""
from math import factorial


def binomial_probability(n, k, p):
    # Функция для вычисления биномиального коэффициента
    binom_coeff = factorial(n) / (factorial(k) * factorial(n - k))
    # Формула биномиального распределения
    prob = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
    return prob


# Количество экспериментов
n = 144
# Количество успехов
k = 70
# Вероятность успеха в одном эксперименте
p = 0.5

# Рассчитываем вероятность
probability = binomial_probability(n, k, p)

print(f"Вероятность, что орел выпадет ровно 70 раз: {probability:.8f}")
