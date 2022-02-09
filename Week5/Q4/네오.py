"""
numbers 를 배열해서 만들 수 있는 수의 최대 개수는
7! = 5040, 6! = 720, 5! = 120...
다 더해도 시간초과가 나지 않습니다.
dfs 를 돌려주면서 모든 생성 가능한 정수에 대해서
소수 판별을 해주면 됩니다.

여기서는 에라토스테네스의 체를 이용해서 소수 판별을 했는데
아마 전에 카카오였나 네이버 공채 코테에서
소수 판별 여러번 하는 문제 나왔는데 거기서는 에라토스테네스로 하면 시간초과가 떴습니다.
에라토스테네스는 큰 범위를 한 번에 다 구하는 거라
여러번 찾을 일이 없다면(?) 같은 수를 반복해서 찾는 경우가 아니라면
그냥 루트 n까지 나눠보면서 해도 됩니다.
"""


def solution(numbers):
    N = len(numbers)
    visited = [False for _ in range(N)]
    possible_set = set()
    is_prime = primes()
    dfs(N, visited, possible_set, is_prime, numbers, [])

    return len(possible_set)


def dfs(N, visited, possible_set, is_prime, numbers, nums):
    if len(nums) > 0:
        number = int("".join(str(numbers[x]) for x in nums))
        if number not in possible_set:
            if is_prime[number]:
                possible_set.add(number)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(N, visited, possible_set, is_prime, numbers,  nums + [i])
            visited[i] = False


def primes():
    e = int("9" * 7)

    is_prime = [True for _ in range(e + 1)]
    is_prime[:2] = [False, False]

    for i in range(2, e + 1):
        if is_prime[i]:
            for j in range(i + i, e, i):
                is_prime[j] = False

    return is_prime