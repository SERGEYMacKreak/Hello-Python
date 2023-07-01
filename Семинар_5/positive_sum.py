# рекурсивная функция sum(a, b), возвращающая сумму двух целых неотрицательных чисел.

def posit_sum(a, b): 
    if (a < 0) or (b < 0):
       return ("Ввели отрицательное число!")
    else:
        if (a <= 0):
            return (b)
        return posit_sum(a - 1, b + 1)