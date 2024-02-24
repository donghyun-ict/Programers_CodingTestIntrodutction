from string import ascii_letters

def solution(my_string):
    answer = 0
    a = list(ascii_letters)
    for i in a:
        my_string = my_string.replace(i, ' ')
    my_string = my_string.split(' ')
    a = ['']
    my_string = [i for i in my_string if i not in a]
    my_string = map(int, my_string)
    return sum(my_string)