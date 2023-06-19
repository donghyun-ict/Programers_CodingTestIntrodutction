import numpy as np
def solution(array):
    a = np.bincount(array).tolist()
    b = max(a)
    c = a.index(b)
    if a.count(b) > 1:
        answer = -1
    else:
        answer = c
    return answer