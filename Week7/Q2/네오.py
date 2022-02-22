"""
완전탐색을 돌립니다.
A가 이기면 최소 경우의 수를,
지면 최대 경우의 수를 리턴합니다.
"""



deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def solution(board, aloc, bloc):
    global N, M
    N = len(board)
    M = len(board[0])
    return dfs(board, aloc, bloc)


def dfs(board, me, partner):
    me_y, me_x = me
    ret = 0

    if board[me_y][me_x] == 1:
        for dy, dx in deltas:
            adj_y, adj_x = me_y + dy, me_x + dx

            if is_valid(adj_y, adj_x) and board[adj_y][adj_x] == 1:
                board[me_y][me_x] = 0
                res = dfs(board, partner, (adj_y, adj_x)) + 1
                board[me_y][me_x] = 1

                if ret % 2 == 0 and res % 2 == 1:
                    ret = res
                elif ret % 2 == 0 and res % 2 == 0:
                    ret = max(ret, res)
                elif ret % 2 == 1 and res % 2 == 1:
                    ret = min(ret, res)

    return ret


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M
