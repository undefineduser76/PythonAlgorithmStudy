def solution(stones, k):
    s = 1
    e = 200000000

    while s <= e:
        m = (s + e) // 2
        if is_possible(stones, m, k):
            s = m + 1
        else:
            e = m - 1
    return e


def is_possible(stones, x, k):
    cnt = 0
    for i in range(len(stones)):
        if stones[i] - x < 0:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True