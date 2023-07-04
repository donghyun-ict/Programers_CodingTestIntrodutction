def solution(n):
    answer = 0
    for i in range(3, n+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                pass
            else:
                count += 1
                break
        if count >= 1:
            answer += 1
    return answer