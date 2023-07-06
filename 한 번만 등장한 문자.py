def solution(s):
    answer = ''
    english = [0 for i in range(26)]
    for i in s:
        english[ord(i) - 97] += 1
    for i in range(len(english)):
        if english[i] == 1:
            answer += chr(i + 97)
    return answer