"""
투 포인터 알고리즘입니다.
N <= 2000 이므로 O(N^2)으로 풀 수 있습니다.
i를 기준으로 양 옆으로 벌려가며 최대값을 확인합니다.
"""


def solution(cookie):
    N = len(cookie)
    max_same = 0
    limits = [lambda x: 0 <= x, lambda x: x < N]

    for i in range(N-1):
        idx = [i, i + 1]
        sums = [cookie[idx[0]], cookie[idx[1]]]

        while True:
            if sums[0] == sums[1]:
                max_same = max(max_same, sums[0])
                c_i, c_d = 0, -1
            elif sums[0] > sums[1]:
                c_i, c_d = 1, 1
            else:
                c_i, c_d = 0, -1

            idx[c_i] += c_d
            if not limits[c_i](idx[c_i]): break
            sums[c_i] += cookie[idx[c_i]]

    return max_same
