"""
그리디 알고리즘을 적용하는 문제입니다.

문제에선 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다고 했습니다.
바꿔 말하면 i번 학생에게 체육복을 빌려줄 수 있는 사람은 i-1 혹은 i+1번 학생입니다.

문제의 답은 '체육수업을 들을 수 있는 학생의 최댓값' 이기 때문에
누가 누구에게 빌렸는지는 중요하지 않습니다.
따라서 문제의 목적은 lost 배열을 돌면서 학생들이 체육복을 빌려줄 수 있는 가능성을 높이는 것입니다.

체육복을 빌려줄 수 있는 가능성을 높이려면 (greedy 하려면)
번호 순서대로 체육복을 빌리면서 최대한 이전 번호의 학생에게 빌려야 합니다.
"""


def solution(n, lost, reserve):
    # 중복을 쉽게 제거하기 위해 각각의 집합을 구합니다.
    set_lost = set(lost)
    set_reserve = set(reserve)

    # lost 는 중복이 제거된 리스트이며, 오름차순으로 정렬됐습니다.
    # 이는 번호 순서대로 체육복을 빌리기 위함입니다.
    lost = sorted(set_lost - set_reserve)

    # reserve 는 중복이 제거된 집합입니다.
    # 여벌이 있어서 타 학생에게 체육복을 빌려줄 수 있는 학생의 집합입니다.
    reserve = set_reserve - set_lost

    # 정답은 '학생 수 - 체육복이 없는 학생 수' 에서 시작합니다.
    # 이 수는 이미 자신의 체육복이 한 벌 이상 있는 학생 수입니다.
    answer = n - len(lost)

    # i번 학생에게 체육복을 빌려줍니다.
    for i in lost:
        # candidates 는 i-1, i+1 중 체육복을 빌려줄 수 있는 학생의 후보군입니다.
        candidates = [i + j for j in [-1, 1] if i + j in reserve]

        if len(candidates) > 0:
            # candidates 중 가장 앞의 학생에게서 체육복을 빌립니다.
            # 체육복을 빌리는 데 성공했으므로 정답에 1을 더해줍니다.
            reserve.remove(candidates[0])
            answer += 1

    return answer
