def manhattan(a, b):
    """
    İki nokta arasındaki Manhattan mesafesini hesaplar.
    """
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))
