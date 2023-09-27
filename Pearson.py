import math

def pearson(array_1, array_2):
   
    """
    Расчет корреляции Пирсона между двумя массивами.

    Args:
     - array_1: первый массив значений
     - array_2: второй массив значений

    Return:
     - Корреляция Пирсона между массивами array_1 и array_2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    # Расчет среднего значения
    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1,array_2)]) / float(len(array_1)) 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation

array_1 = [1,4,6,8,10,17,99]
array_2 = [5,9,8,5,3,8,2]

correlation = round(pearson(array_1, array_2),4)
print(f"Корреляция Пирсона: {correlation}")