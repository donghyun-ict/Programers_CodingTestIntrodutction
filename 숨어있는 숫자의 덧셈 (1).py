def solution(my_string):
    answer = 0
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in l:
            answer += int(i)
    return answer