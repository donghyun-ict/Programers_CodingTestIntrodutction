def solution(num, k):
    try:
        answer = str(num).index(str(k))
        return answer + 1
    except:
        return -1