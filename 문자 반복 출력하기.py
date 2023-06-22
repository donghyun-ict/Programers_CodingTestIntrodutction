def solution(my_string, n):
    answer = []
    my_string_list = list(my_string)
    for i in my_string_list:
        answer.append(i * n)
    answer = ''.join(answer)
    return answer