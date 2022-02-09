'''
문제 풀이
1. N보다 s의 크기가 큰 경우는 불가능해서 큰 경우 -1 리턴한다.
2. n개 나눈다..
3. 그리고 나머지는 내머지 만큼 각 인덱스 +1 씩 해준다.
'''

def solution(n, s):
    # 자연수 n개의 합으로 n보다 작은 s를 만들 수는 없으므로 [-1]을 리턴한다
    if n > s: return [-1]
    result = []
    # s를 n으로 나눈 몫이 n개이도록 초기값을 정한다.
    initial = s // n
    for _ in range(n):
        result.append(initial)
    idx = len(result) - 1
    # s를 n으로 나눈 몫에서 나머지만큼 각 값에 1씩 더해준다.
    for _ in range(s % n):
        result[idx] += 1
        idx -=1
    return result

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))