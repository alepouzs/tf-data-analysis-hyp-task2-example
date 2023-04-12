import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = MMD().test(x, y)
    return pvalue < 0.06
