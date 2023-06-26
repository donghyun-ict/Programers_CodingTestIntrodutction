def solution(my_string):
    answer = ''
    l = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in l:
            answer += i
    return answer