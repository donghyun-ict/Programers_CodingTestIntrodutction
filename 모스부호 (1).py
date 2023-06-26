def solution(letter):
    answer = ''
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letter = letter.split(' ')
    for i in letter:
        answer += chr(morse_code.index(i) + 97)
    return answer