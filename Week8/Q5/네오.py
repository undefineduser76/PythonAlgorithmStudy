import math


def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(1, N):
        for j in range(N - i):
            dp[j][j + i] = math.inf
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + matrix_sizes[j][0] * matrix_sizes[k][1] * matrix_sizes[j + i][1])

    return dp[0][N - 1]


matrix_sizes = [[5,3],[3,10],[10,6]]
print(solution(matrix_sizes))