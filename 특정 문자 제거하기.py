def solution(my_string, letter):
    answer = []
    for i in my_string:
        checker = 0
        for j in letter:
            if i == j:
                checker = 1
        if checker == 0:
            answer.append(i)
    answer = ''.join(answer)
    return answer