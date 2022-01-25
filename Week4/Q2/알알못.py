'''
네트워크
문제요악
1. 네트워크: 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미
2. 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers
3. 네트워크 영역 개수 구하기

문제 풀이
1. dfs 방법으로 푼다.
2. 아무노드에서 시작에서 방문한다.
3. 방문 끝나면 개수 +1
4. 방문하지 않은 노드에서 다시 출발한다.
'''

def dfs(root, visited, computers):
    visited[root] = True # 방문여부 표시
    for i in range(len(visited)): # len(visited) = n
        # root-i를 잇는 간선이 있고, 정점i를 아직 방문 안했다면
        if computers[root][i] and not visited[i]: 
            computers[root][i], computers[i][root] = 0, 0 # 간선 방문후 삭제(무방향그래프니까, 양쪽 모두 변경)
            dfs(i, visited, computers) # 정점i의 이웃노드 탐색을 위해 dfs()호출

def solution(n, computers):
    answer = 0 # 네트워크 개수
    visited = [False]*n # 방문여부 판단
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않은 정점
            dfs(i, visited, computers) 
            answer += 1 # 네트워크 개수 증가
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))