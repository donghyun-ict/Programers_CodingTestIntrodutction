import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    for i in range(max(denom1, denom2), denom1 * denom2 + 1):
        if i % denom1 == 0 and i % denom2 == 0:
            m = i
            break
    numer1 *= m // denom1
    numer2 *= m // denom2
    n = numer1 + numer2
    g = math.gcd(n, m)
    answer.append(n//g)
    answer.append(m//g)
    return answer