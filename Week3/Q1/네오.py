"""
비트마스크 + dp 문제입니다.
방문여부 체크가 중점입니다.
'abcd 노드를 방문한 적이 있을 때 x 번 노드를 방문한 적이 있는가?'를 방문 여부로 체크해줘야 합니다.
visited[x][abcd] 이때 abcd 는 비트마스크로 해결합니다.
"""


max_sheep = 0


def solution(info, edges):
    make_graph(len(info), edges)
    dfs(0, 1, 0, 1, info)
    return max_sheep


# 그래프를 만듦
def make_graph(n, edges):
    global graph, visited
    graph = [[] for _ in range(n)]
    visited = [[False for _ in range(2 ** n)] for _ in range(n)]

    for edge in edges:
        [a, b] = edge
        graph[a].append(b)
        graph[b].append(a)


def dfs(now, sheep, wolf, so_far, info):
    global max_sheep
    max_sheep = max(max_sheep, sheep)

    for adj in graph[now]:
        # 만약 adj 노드를 방문할 시 노드 방문 비트 구하기
        if_visit = so_far | (1 << adj)

        # if_visit 대로 방문한 상태에서 adj 노드를 방문한 적이 없을 경우
        if not visited[adj][if_visit]:
            visited[adj][if_visit] = True

            # so_far 에 adj 번쨰 비트가 0일 경우 (첫방문)
            if so_far & (1 << adj) == 0:
                # 양과 늑대 개수를 늘려줌
                next_sheep = sheep + (not info[adj])
                next_wolf = wolf + info[adj]
            else:
                next_sheep = sheep
                next_wolf = wolf

            # 양이 늑대보다 많으면 다음 탐색 실행
            if next_wolf < next_sheep:
                dfs(adj, next_sheep, next_wolf, if_visit, info)


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))