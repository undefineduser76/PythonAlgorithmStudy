"""
몇 번째부터 시작할지 모름...
원을 그린다고 했을 때, (첫번째와 마지막 글자가 연결)
A가 아닌 글자들의 시퀀스 중,
가장 길이가 짧은 시퀀스를 구하려면,
가장 처음으로 A가 아닌 글자의 인덱스부터 시작해서 각각의 A가 아닌 글자들과의 사이 거리를 구한다.
다 돌았으면 마지막과 처음의 사이를 구한다... (이때의 거리는 N-j+i)
사이들 중 최대값을 가지게 하는 인덱스 쌍... 이 사이가 가장 넓기 때문에,
이것이 아닌 구간을 도는 것이 가장 최소값을 가지게 하는 시퀀스이다.
그것이 (a, b)라고 한다면, b부터 a까지 돌아야 한다.
"""


def solution(name):
    answer = [0]
    N = len(name)
    not_a = [i for i in range(N) if name[i] != 'A']

    if len(not_a) == 0:
        return 0

    distances = []
    for i in range(len(not_a) - 1):
        distances.append([not_a[i + 1] - not_a[i], [not_a[i], not_a[i + 1]]])
    distances.append([N - not_a[-1] + not_a[0], [not_a[-1], not_a[0]]])

    distances.sort(key=lambda x: -x[0])

    [a, b] = distances[0][1]

    now = b
    while now != a:
        change_character(name[now], answer)
        answer[0] += 1
        now = (now + 1) % N
    change_character(name[now], answer)

    return answer[0]


def change_character(x, answer):
    if x != 'A':
        answer[0] += min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)
