"""
로봇 두 개를 평행이동, 회전시킨다는 점에서
일반적인 bfs 보다 더 까다로운 문제였습니다.
막 풀다보면 예외처리 하는 데에 시간이 걸릴 수가 있어서
로봇을 취급하고 이동시키는 단 한 가지 방법을 고안해야 합니다.
저의 경우엔 로봇에서 항상 왼쪽 위를 primary 로 뒀습니다.
회전의 경우에는, 먼저 중점(center)과 회전할 부분(to_turn)을 정하고,
중점에서 회전할 부분까지의 변화량을 deltas 에서 찾은 뒤
거기서부터 시계방향이면 순방향으로 회전, 아니면 역순으로 회전시킵니다.
회전하다가 벽이 나오면 그 방향대로는 회전이 불가능합니다.
"""


from collections import deque


HORIZONTAL = 0
VERTICAL = 1

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(board):
    global N
    N = len(board)

    # 왼쪽 상단에서부터 시작하며 로봇은 가로로 놓여있음.
    will_visit = deque([[(0, 0), HORIZONTAL, 0]])

    # visited[y][x][i]: (y, x) 에 primary 가 i 형태로 존재한 적이 있음
    visited = [[[False for _ in range(2)] for _ in range(N)] for _ in range(N)]

    while len(will_visit) > 0:
        [now_primary, now_shape, now_cnt] = will_visit.popleft()
        now_secondary = add(now_primary, deltas[now_shape])
        now_block = (now_primary, now_secondary)

        # 도착 시 종료
        if is_arrived(now_block):
            return now_cnt

        # 위 아래 왼쪽 오른쪽 평행이동
        for i in range(4):
            next_primary = translate(board, now_block, i)
            next_move(next_primary, now_shape, now_cnt + 1, visited, will_visit)

        # primary 를 돌리면 True, primary 가 아닌 부분을 돌리면 False, 시계방향이면 1, 반시계방향이면 -1
        cases = [(True, 1), (True, -1), (False, 1), (False, -1)]
        for i in range(4):
            next_primary = rotate(board, now_block, cases[i][0], cases[i][1])
            next_move(next_primary, not now_shape, now_cnt + 1, visited, will_visit)


# 다음에 위치할 primary 가 유효한 위치인지 파악 후 큐에 추가
def next_move(next_primary, next_shape, next_cnt, visited, will_visit):
    if next_primary is not None and not visited[next_primary[0]][next_primary[1]][next_shape]:
        visited[next_primary[0]][next_primary[1]][next_shape] = True
        will_visit.append([next_primary, next_shape, next_cnt])


# direction 대로 평행이동
def translate(board, block, direction):
    primary, secondary = block
    primary_moved = add(primary, deltas[direction])
    secondary_moved = add(secondary, deltas[direction])

    # 이동한 두 부분이 유효함
    if is_valid(board, primary_moved) and is_valid(board, secondary_moved):
        return primary_moved
    else:
        return None


def rotate(board, block, turn_primary, clockwise):
    primary, secondary = block
    to_turn, center = (primary, secondary) if turn_primary else (secondary, primary)

    # 회전할 부분 - 중점 변화량
    x = sub(to_turn, center)
    # deltas 에서 해당 변화량의 위치
    idx = deltas.index(x)

    # 마지막 변화량부터 돌림
    for i in range(1, 3):
        to_turn = add(to_turn, deltas[(idx + clockwise * i) % 4])
        # 돌리는 도중에 유효하지 않은 위치 발견
        if not is_valid(board, to_turn):
            return None

    return sorted([to_turn, center])[0]


# 로봇이 우측 하단에 위치하는지 검사
def is_arrived(block):
    for b in block:
        if b == (N - 1, N - 1):
            return True
    return False


# 한 지점이 유효한지 검사
def is_valid(board, pos):
    return 0 <= pos[0] < N and 0 <= pos[1] < N and board[pos[0]][pos[1]] != 1


# 위치값 더함
def add(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))


# 위치값 뺌
def sub(a, b):
    return tuple(a[i] - b[i] for i in range(len(a)))
