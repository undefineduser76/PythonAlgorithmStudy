"""
첫번째 수는 (n-1)!번 지날 때마다 바뀝니다.
이를 일반화하면 i번째 수는 (n-i)!번 지날 때마다 바뀝니다.
i번째 수는 현재 남은 수 중에서 (남은 순번 / (n-i)!)번째 수입니다.
"""


from math import ceil, factorial


def solution(n, k):
    nums = [i for i in range(1, n+1)]
    answer = []

    for i in range(n-1, 0, -1):
        nf = factorial(i)
        to_append = nums[ceil(k / nf) - 1]
        answer.append(to_append)
        nums.remove(to_append)
        k = k % nf

    answer.append(nums[0])

    return answer
