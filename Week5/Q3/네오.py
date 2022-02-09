"""
a b c 에서 b를 살린다고 할 때

a < b < c 가능   a:b에서 a 터뜨리고 b:c에서 c 터뜨림
a < b > c 불가능  어딜 먼저 터뜨리더라도 b를 터뜨릴 수 밖에 없음
a > b < c 가능   a:b에서 a 터뜨리고 b:c에서 c 터뜨림
a > b > c 가능   a:b에서 a, b:c에서 c 터뜨림

x[i]가 생존 가능한지 알아보려면
x[:i]에서 가장 작은 수, 그리고 x[i+1:]에서 가장 작은 수와 x[i] 중
x[i]가 가장 큰 수가 아니면 됩니다.

만약 i가 왼쪽이나 오른쪽 끝이라면 최대값을 넣어줍니다.
"""


MAX = 1000000001


def solution(a):
    min_min = [[MAX for _ in range(len(a))] for _ in range(2)]
    n = len(a)
    sweep(0, n, 1, a, min_min[0])
    sweep(n-1, -1, -1, a, min_min[1])

    answer = 0
    for i in range(n):
        if not (a[i] > min_min[0][i] and a[i] > min_min[1][i]):
            answer += 1

    return answer


def sweep(s, e, df, a, min_min):
    now_min = MAX

    for i in range(s, e, df):
        min_min[i] = now_min
        if a[i] < now_min:
            now_min = a[i]
