'''
문제 풀이
1. 스택 만든다
2. number를 순회 한다.
3. k보다 크고 앞에 숫자 보다 크면 리턴하고 뺀다.
5. k가 0 이상이면 스택에서 제거한다.
'''

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))