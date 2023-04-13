import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = cramervonmises_2samp(x, y)
    return pvalue < 0.06
