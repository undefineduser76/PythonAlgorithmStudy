"""
visited 가 set 인 문제입니다.
'최소' 단계를 내는 거라 bfs 를 쓰면 편합니다.
"""

from collections import deque


def solution(begin, target, words):
    will_visit = deque([(begin, 0)])
    n = len(begin)
    visited = set()

    while len(will_visit) > 0:
        now_word, now_cnt = will_visit.popleft()

        if now_word == target:
            return now_cnt

        for word in words:
            if word not in visited:
                is_convertable = sum([1 for i in range(n) if now_word[i] != word[i]]) == 1
                if is_convertable:
                    visited.add(word)
                    will_visit.append((word, now_cnt + 1))

    return 0