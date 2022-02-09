'''
문제 풀이
1. 각 배열 개수 (n -1) factorial 계산한다.
2. 배열의 몇번째 인덱스 뺄 것은 찾는다.
3. 배열의 개수 다 없어 질때 까지 반복한다.
'''

import math

def solution(n, k):
    answer = []
    array = list(range(1, n+1))
    count = 1
    
    while n:
        temp = math.factorial(n) // n
        index = k // temp
        k = k % temp
        if k == 0:
            answer.append(array.pop(index - 1))
        else:
            answer.append(array.pop(index))
        print(answer, temp, index, k)
        n -= 1
    return answer

print(solution(3, 5))
