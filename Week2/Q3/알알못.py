'''
메뉴 리뉴얼
문제 요약
- 이전 각 손님 주문할 때 가장 많이 함께 주문한 단품메뉴를 조합해서 코스요리로 메뉴 구성
- 코스요리 메뉴는 최소 2가지 이상 단품메뉴로 구성
- 최소 2명 이상 손님으로 기록이 있음
- orders는 각 손님들이 주문한 단품메뉴들
- course는 단품 메뉴들의 갯수
- 갯수중 많이 나온것 추가한다.

문제 풀이
1. 각 코스들을 조합으로 뽑아내서 추가한다.
2. 각 코스에서 최종으로 추가한 것을 counter 함수로 갯수를 구한다.
3. 조합된 메뉴가 2개이상이고 조합 매뉴 갯수 최고인것을 구한다.
'''


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        count = [] # 각 코스갯수 마다 조합할 리스트 변수
        for order in orders:
            order = combinations(sorted(order), num) # 문자 순대로 코스갯수 조합한다.
            count += order
        courseFood = Counter(count) # 각 주문한것을 조합한것을 갯수를 구한다.
        # 조건에 맞게 추가한다.
        answer += [''.join(key) for key, value in courseFood.items() if (value > 1 and  max(courseFood.values()) == value)]
            
    return sorted(answer) # 문자열 순서대로 정렬해서 리턴한다.


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))