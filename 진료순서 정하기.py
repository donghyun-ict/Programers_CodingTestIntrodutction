def solution(emergency):
    answer = []
    emergency2 = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(emergency2.index(i) + 1)
    return answer