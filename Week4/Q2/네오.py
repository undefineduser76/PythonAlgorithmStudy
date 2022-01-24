"""
dfs/bfs 문제입니다.
visit 표시가 안 돼있는 노드마다 dfs 를 돌려줍니다.
dfs 를 돌려주면서 방문한 노드에 visit 표시를 합니다.
dfs 를 시작할 때마다 카운트를 셉니다.
"""


def solution(n, computers):
    visited = [False for _ in range(n)]

    def dfs(v):
        for adj in range(n):
            if computers[v][adj] and not visited[adj]:
                visited[adj] = True
                dfs(adj)

    answer = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer += 1
            dfs(i)

    return answer