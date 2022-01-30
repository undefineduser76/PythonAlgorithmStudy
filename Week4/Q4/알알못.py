'''
문제요약
1."ICN" 공항에서 출발합니다.
2. 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return

문제풀이
1. 키 : 값 형태 구조로 바꾼다.
2.  bfs 방식을 사용한다.
3. stack을 'INC' 부터 시작해서 키값 찾으면서 여행 경로를 담는다.

'''

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    for key in routes.keys():
        routes[key].sort(reverse=True)
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))