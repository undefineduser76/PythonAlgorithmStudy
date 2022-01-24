"""
bfs 로 풀긴 했으나 dfs 로 풀면 더 빨리 풀 수 있는 문제입니다.
다른 문제와 달리 노드가 아닌 모든 간선을 방문하는 문제인데
문제를 잘 읽어보면 티켓이 중복이 되지 않는다는 말이 없으므로
한 티켓이 여러장일 수도 있기 때문에, 그리고 문제에서 '경로' 를 물어봐서 visit 체크를
전체적으로 해주면 안 되기 때문에 티켓 개수에 대한 정보를 매 노드로 전달해줘야 합니다.
dfs 를 하면 티켓 개수 변경 후 재귀 호출하고 복귀 후 다시 원상복구 해주면 되는데
bfs 특성상 정보를 모두 전달해줘야 해서 복사하는데 시간이 걸립니다.
문제의 시간이 넉넉하게 주어져서 bfs 로 풀어도 통과는 됩니다.
"""


from collections import deque, defaultdict
from copy import deepcopy


def solution(tickets):
    graph, ticket_dict = make_graph(tickets)
    will_visit = deque([("ICN", deepcopy(ticket_dict), ["ICN"])])

    while len(will_visit) > 0:
        now_airport, tickets_left, now_path = will_visit.popleft()
        if len(tickets_left) == 0:
            return now_path

        for adj in graph[now_airport]:
            line = (now_airport, adj)
            if line in tickets_left.keys() and tickets_left[line] > 0:
                next_tickets = deepcopy(tickets_left)
                next_tickets[line] -= 1
                if next_tickets[line] == 0:
                    next_tickets.pop(line)
                will_visit.append((adj, next_tickets, now_path + [adj]))


def make_graph(tickets):
    graph = defaultdict(lambda : [])
    ticket_dict = defaultdict(lambda : 0)

    for from_, _to in tickets:
        graph[from_].append(_to)
        ticket_dict[(from_, _to)] += 1

    for from_ in graph.keys():
        graph[from_].sort()

    return graph, ticket_dict