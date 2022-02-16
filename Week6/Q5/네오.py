"""
파라매트릭 서치 문제입니다.
is_possible 함수는 n개 이하를 지워서 거리 사이를 x 이상으로 할 수 있는지를 반환합니다.
되면 x를 좀 키워도 되고, 안 되면 x를 줄여야 합니다.
"""


def solution(distance, rocks, n):
    rocks = [0] + rocks + [distance]
    rocks.sort()
    s = min([rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)])
    e = max([rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)])

    while s <= e:
        m = (s + e) // 2

        if is_possible(rocks, m, n):
            s = m + 1
        else:
            e = m - 1

    return e


def is_possible(rocks, x, n):
    erased = 0
    prev = rocks[0]

    for i in range(1, len(rocks)):
        if rocks[i] - prev < x:
            erased += 1
            if erased > n:
                return False
        else:
            prev = rocks[i]

    return True
