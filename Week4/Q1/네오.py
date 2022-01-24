"""
dfs/bfs 문제입니다.
저는 bfs 문제로 풀었습니다.
주의해야 할 점으로, visited 체크를 하면 안 됩니다.
도중에 target 넘버에 도달하는 경우도 있기 때문입니다.
"""


from collections import deque


def solution(numbers, target):
    will_visit = deque([[0, 0]])
    answer = 0

    while len(will_visit) > 0:
        [now_number, now_i] = will_visit.popleft()

        if now_i >= len(numbers):
            if now_number == target:
                answer += 1
            continue

        will_visit.append([now_number + numbers[now_i], now_i + 1])
        will_visit.append([now_number - numbers[now_i], now_i + 1])

    return answer
