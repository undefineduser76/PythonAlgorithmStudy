'''
문제 풀이
1. 배열의 어떤 수든 자신의 왼쪽 혹은 오른쪽 어느 한 쪽 방향에 자기보다 큰 수만 존재할 시, 마지막까지 남기는 것이 가능합니다.
2. 배열의 앞과 뒤에서 각각 검사를 진행하여 한쪽 방향에서 자신이 가장 작을 시, 정답을 담는 result 배열에 True를 담는다.
3. sum(result)으로 최후까지 남기는 것이 가능한 풍선들의 개수를 return.
'''

def solution(a):
    result = [False for _ in range(len(a))]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))