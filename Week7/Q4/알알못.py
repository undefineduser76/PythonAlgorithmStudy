import heapq

def solution(land, height):
    N = len(land)  # land의 길이

    visited = [[False for _ in range(N)] for _ in range(N)]  # 방문했는지
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 이동할 방향
    queue = [] # 뀨?

    queue.append((0, 0, 0))  # 큐에 초기값 지정
    visit_count = 0  # 방문 횟수
    max_count = N * N  # 최대 방문 가능 횟수
    value = 0  # 사다리 설치비용

    while(visit_count < max_count):
        print(queue)
        v, y, x = heapq.heappop(queue)
        if visited[y][x]:  # 이미 방문했다면
            continue # 넘긴다
        visited[y][x] = True  # 방문 완료

        visit_count += 1  # 방문 횟수 + 1
        value += v  # 사다리 설치 비용 추가

        c_height = land[y][x]  # 현 좌표의 height
        for ay, ax in move:
            ny, nx = y + ay, x + ax  # 이동한 좌표의 y, x
            if move2(ny, nx, N, visited):  # 이동 가능한지 체크
                n_height = land[ny][nx]  # 이동한 좌표의 height

                if abs(n_height - c_height) > height:  # 사다리가 필요한 경우 필요한 비용을 값으로 줌 
                    heapq.heappush(queue, (abs(n_height - c_height), ny, nx))
                else:  # 사다리 없이 방문 가능한 좌표는 비용은 0을 준다
                    heapq.heappush(queue, (0, ny, nx))
    return value