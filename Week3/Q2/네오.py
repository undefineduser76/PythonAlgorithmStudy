"""
다익스트라를 이용하는 문제입니다.
n <= 200 이므로,
i -> S 까지의 거리를 다 구해도 (i <= n)
시간초과가 나지 않습니다.
이 코드는 플로이드-와샬 알고리즘으로
모든 쌍의 거리를 구한 후 합승 택시 요금을 구합니다.
"""

import math


def solution(n, s, a, b, fares):
    adj_matrix = get_adj_matrix(n, fares)
    floyd(adj_matrix)
    answer = min([try_here(s, i, a, b, adj_matrix) for i in range(1, n + 1)])
    return answer


def get_adj_matrix(n, fares):
    adj_matrix = [[math.inf for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        adj_matrix[i][i] = 0
    for [c, d, f] in fares:
        adj_matrix[c][d] = f
        adj_matrix[d][c] = f
    return adj_matrix


def floyd(adj_matrix):
    for k in range(1, len(adj_matrix)):
        for i in range(1, len(adj_matrix)):
            for j in range(1, len(adj_matrix)):
                new_dist = adj_matrix[i][k] + adj_matrix[k][j]
                if adj_matrix[i][j] > new_dist:
                    adj_matrix[i][j] = new_dist


def try_here(s, x, a, b, adj_matrix):
    together = adj_matrix[s][x]
    a_dist = adj_matrix[x][a]
    b_dist = adj_matrix[x][b]
    total_cost = together + a_dist + b_dist
    return total_cost