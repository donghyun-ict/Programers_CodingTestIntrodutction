def solution(array, n):
    l = []
    b = []
    for i in array:
        l.append(abs(n - i))
    a = list(filter(lambda x: l[x] == min(l), range(len(l))))
    for i in a:
        b.append(array[i])
    return min(b)