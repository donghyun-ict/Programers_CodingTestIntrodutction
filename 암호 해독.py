def solution(cipher, code):
    answer = ''
    cipher = list(cipher)
    for i in range(code - 1, len(cipher), code):
        answer += str(cipher[i])
    return answer