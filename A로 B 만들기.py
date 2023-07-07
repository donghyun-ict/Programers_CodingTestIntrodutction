def solution(before, after):
    answer = 0
    before = sorted(list(before))
    after = sorted(list(after))
    if after == before:
        answer = 1
    return answer