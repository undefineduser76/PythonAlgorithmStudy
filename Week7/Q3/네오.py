"""
N이 크면 마나커 알고리즘을 써야 합니다.
N이 상대적으로 작아서 그냥 했습니다.
"""


from math import ceil


def solution(s):
    even = False
    if len(s) % 2 == 0:
        s = ''.join([x + '#' for x in s[:-1]]) + s[-1]
        even = True
    return get_max_len(s, even)


def get_max_len(s, even):
    max_len = 0

    for i in range(len(s)):
        now_len = 1
        start = i - 1
        end = i + 1

        while 0 <= start and end < len(s):
            if s[start] != s[end]:
                break
            start -= 1
            end += 1
            now_len += 2

        if even:
            if s[start + 1] == '#':
                now_len = (now_len - 1) // 2
            else:
                now_len = ceil(now_len / 2)
        max_len = max(max_len, now_len)

    return max_len


s = "aabbbc"
print(solution(s))
