"""
앞에서 작은 값들을 k개 빼줍니다.
"""


def solution(number, k):
    stack = []
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)

    return "".join(stack[:len(stack) - k])