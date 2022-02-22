"""
차이가 height 이하인 것들끼리 클러스터로 묶어주고 번호를 표시합니다.
클러스터 하나를 노드로 간주하고 높이 차를 클러스터 간의 엣지의 가중치로 간주하는 그래프가 만들어집니다.
해당 그래프에 대해서 크루스칼 혹은 프림 알고리즘으로 최소 스패닝 트리를 그려줍니다.
"""


from collections import deque
import heapq


deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(land, height):
    global N
    N = len(land)
    clusters, num_cluster = get_clusters(land, height)
    edge_queue = get_edge_queue(land, clusters)
    min_ladder = kruskal(edge_queue, num_cluster)
    return min_ladder


def get_clusters(land, height):
    visited = [[False for _ in range(N)] for _ in range(N)]
    clusters = [[0 for _ in range(N)] for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                get_cluster((i, j), visited, clusters, num, land, height)
                num += 1
    return clusters, num


def get_cluster(start, visited, clusters, num, land, height):
    visited[start[0]][start[1]] = True
    clusters[start[0]][start[1]] = num
    will_visit = deque([start])
    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()
        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if abs(land[now_y][now_x] - land[adj_y][adj_x]) > height:
                continue
            visited[adj_y][adj_x] = True
            clusters[adj_y][adj_x] = num
            will_visit.append((adj_y, adj_x))


def get_edge_queue(lands, clusters):
    edge_queue = []
    for i in range(N):
        for j in range(N):
            for dy, dx in deltas:
                adj_y, adj_x = i + dy, j + dx
                if is_valid(adj_y, adj_x):
                    if clusters[i][j] != clusters[adj_y][adj_x]:
                        heapq.heappush(edge_queue, (abs(lands[i][j] - lands[adj_y][adj_x]), clusters[i][j], clusters[adj_y][adj_x]))
    return edge_queue


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    min_parent = min(a, b)
    parents[a] = min_parent
    parents[b] = min_parent


def find(parents, x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]


def is_group(parents, a, b):
    a_parent = find(parents, a)
    b_parent = find(parents, b)
    return a_parent == b_parent


def kruskal(edge_queue, num_cluster):
    parents = [i for i in range(num_cluster)]
    min_ladder = 0

    while len(edge_queue) > 0:
        weight, a, b = heapq.heappop(edge_queue)
        if not is_group(parents, a, b):
            union(parents, a, b)
            min_ladder += weight

    return min_ladder


def is_valid(i, j):
    is_in = lambda x: 0 <= x < N
    return is_in(i) and is_in(j)
