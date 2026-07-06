import math

def minkowski(a, b, p):
    """
    Hem Manhattan (p=1) hem de Euclidean (p=2) için genel formül.
    """
    return sum(abs(val1 - val2) ** p for val1, val2 in zip(a, b)) ** (1/p)

def manhattan(a, b):
    # Testlerin beklediği 'manhattan' fonksiyonu
    return minkowski(a, b, p=1)

def euclidean(a, b):
    # Testlerin beklediği 'euclidean' fonksiyonu
    return minkowski(a, b, p=2)