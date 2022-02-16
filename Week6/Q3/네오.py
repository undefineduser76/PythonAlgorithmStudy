"""
완전탐색을 어떻게 쉽게 구현하는지가 관건인 문제입니다.
"""


def solution(key, lock):
    global N, M
    N = len(lock)
    M = len(key)
    holes = N ** 2 - sum([sum(l) for l in lock])

    if holes == 0:
        return True

    for i in range(-M + 1, N):
        for j in range(-M + 1, N):
            for r in range(4):
                if is_right(i, j, key, lock, holes):
                    return True
                key = rotate(key)

    return False


def rotate(key):
    rotated = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotated[j][M - i - 1] = key[i][j]
    return rotated


def is_right(i, j, key, lock, holes):
    filled_hole = 0

    for k in range(M):
        for l in range(M):
            if 0 <= i + k < N and 0 <= j + l < N:
                if key[k][l] != lock[i + k][j + l]:
                    if key[k][l] == 1:
                        filled_hole += 1
                else:
                    return False

    return True if filled_hole == holes else False
