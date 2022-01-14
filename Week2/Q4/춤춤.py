# 거리두기 확인하기
'''
입출력 예시
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1, 0, 1, 1, 1]
'''

from collections import deque

def bfs(p):
    # "P"부터 탐색하기 위해 "P"가 있는 좌표들을 모음
    start = []

    # P가 시작인 좌표
    for i in range(5):
        for j in range(5):
            if p[i][j] == "P":
                start.append([i,j])

    # P로 시작하는 좌표들
    for s in start:
        # 큐에 좌표들을 쌓음
        queue = deque([s])

        # 방문한 곳을 처리하는 리스트
        visited = [[0]*5 for i in range(5)]

        # 경로 길이 계산하는 리스트
        distance = [[0]*5 for i in range(5)]

        # P가 있는 좌표는 방문처리
        visited[s[0]][s[1]] = 1

        while queue:
            # 맨 처음부터 하나씩 꺼냄
            x,y = queue.popleft()

            # 좌우 움직이는 좌표
            dx = [-1, 1, 0, 0]
            
            # 상하 움직이는 좌표
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 이동한 x,y 좌표가 0보다 작거나 5 이상일 경우 무시
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                
                # 한번도 방문하지 않은 곳에 대해
                elif visited[nx][ny] == 0:

                    # "O"이면 큐에 좌표를 추가 / 방문에 1 추가 / 거리에 1을 더함
                    if p[nx][ny] == "O":
                        queue.append([nx,ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    
                    # "P"이고 거리가 1보다 작거나 같으면 0을 리턴
                    elif p[nx][ny] == "P" and distance[x][y] <= 1:
                        return 0
        
    return 1


        
def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer