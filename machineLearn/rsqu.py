# metrics.py

import numpy as np


def r_squared(y_true, y_pred):
    """
    R-kare (R-squared) değerini hesaplar.

    Parametreler:
    y_true: Gerçek değerler (numpy array veya liste).
    y_pred: Modelin tahmin ettiği değerler (numpy array veya liste).

    Döndürür:
    R-kare değeri (float).
    """
    y_mean = np.mean(y_true)
    tss = np.sum((y_true - y_mean) ** 2)  # Toplam kareler toplamı
    rss = np.sum((y_true - y_pred) ** 2)  # Artık kareler toplamı
    return 1 - (rss / tss)
