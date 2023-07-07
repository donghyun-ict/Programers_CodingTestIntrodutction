def solution(my_string):
    answer = ''
    l = []
    for i in my_string:
        i = ord(i)
        if i <= 90:
            i += 32
        l.append(i)
    l.sort()
    for i in l:
        answer += chr(i)
    return answer