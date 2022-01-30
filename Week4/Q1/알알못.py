'''
타켓넘버
문제요약
1. n개의 음이 아닌 정수
2. 이 수를 적절히 덧셈 뺄셈으로 타켓 넘버 생성
3. 방법 구하기

문제 풀이
1. BFS 방법 사용
2. queue 사용하기위해 deque 사용
3. numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가해준다.
4. 결국 leaves리스트에 모든 계산 결과가 담기게 된다. 이후 target값과 비교해서 결과 출력.

'''

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution([1,1,1,1,1], 3))