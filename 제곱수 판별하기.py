def solution(n):
    answer = 2
    i = 1
    while i**2 <= n:
        if i**2 == n:
            answer = 1
            break
        i += 1
    return answer