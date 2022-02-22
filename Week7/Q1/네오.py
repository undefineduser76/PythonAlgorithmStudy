"""
N <= 2000 인데
시간 범위는 엄청 커서
N^2로 풀어야 하는 그리디 문제입니다.
만약 시간 범위가 작았다면 누적 합 문제로 N으로 풀 수 있을 것 같습니다.
"""


import re

one_second = 1000


def solution(lines):
    requests = get_requests(lines)
    max_throughput = 0

    for [start, end] in requests:
        max_throughput = max(max_throughput, get_throughput(start, requests), get_throughput(end, requests))

    return max_throughput


def get_requests(lines):
    requests = []
    for line in lines:
        h, m, s, elapsed = map(float, re.search("2016-09-15 (\d{2}):(\d{2}):(\d{2}\.\d+) (\d\.?\d*)s", line).groups())
        end = h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000
        start = end - (elapsed * 1000 - 1)
        requests.append([start, end])
    return requests


def get_throughput(term_start, requests):
    term_end = term_start + 1000
    throughput = 0
    for [start, end] in requests:
        if start < term_end and end >= term_start:
            throughput += 1
    return throughput


lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]



print(solution(lines))