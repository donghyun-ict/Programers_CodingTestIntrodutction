def solution(i, j, k):
    answer = 0
    for a in range(i, j + 1):
        if str(k) in str(a):
            answer += 1
            print(a)
    return answer

solution(1, 13, 1)