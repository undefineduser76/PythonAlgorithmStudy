def solution(board, skill):
    global N, M
    answer = 0
    N = len(board)
    M = len(board[0])

    deltas = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for [type, r1, c1, r2, c2, degree] in skill:
        if type == 1: degree *= -1
        deltas[r1][c1] += degree
        deltas[r1][c2 + 1] -= degree
        deltas[r2 + 1][c1] -= degree
        deltas[r2 + 1][c2 + 1] += degree

    for i in range(N):
        for j in range(M):
            deltas[i][j+1] += deltas[i][j]

    for j in range(M):
        for i in range(N):
            deltas[i+1][j] += deltas[i][j]

    for i in range(N):
        for j in range(M):
            if deltas[i][j] + board[i][j] > 0:
                answer += 1

    return answer