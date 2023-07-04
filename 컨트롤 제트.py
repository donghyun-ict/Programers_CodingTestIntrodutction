def solution(s):
    answer = 0
    s = str.split(s)
    s_num = []
    s_Z = []
    for i in range(len(s)):
        if s[i] == 'Z':
            s_Z.append(int(s[i - 1]))
        else:
            s_num.append(int(s[i]))
    answer = sum(s_num) - sum(s_Z)
    return answer