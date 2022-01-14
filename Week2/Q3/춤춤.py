# 메뉴리뉴얼
'''
입출력 예제
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
[2,3,4]	
["AC", "ACDE", "BCFG", "CDE"]

["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
[2,3,5]	
["ACD", "AD", "ADE", "CD", "XYZ"]

["XYZ", "XWY", "WXA"]	
[2,3,4]	
["WX", "XY"]
'''

from itertools import combinations
from collections import Counter

def solution(orders, course): 
    answer = []

    # 조합 수를 반복
    for c in course: # [2,3,4]
        temp = []
        
        # 각 주문에 대해 알파벳순서로 정렬 후 조합 수만큼 조합 생성
        for order in orders: # "ABCFG"
            comb = combinations(sorted(order), c) # "ABCFG", [2,3,4]
            temp += comb # [('A','B'), ('A','C'),...]
        
        # 각 조합을 key로, 개수를 value로 가진 딕셔너리 생성
        c_dict = Counter(temp)

        # c_dict에 원소가 있을 때 
        if c_dict:
            maxi = max(list(c_dict.values()))
            # 가장 큰 수가 2 이상이면 문자를 결합해 리스트에 추가
            if maxi >= 2:
                for key in c_dict:
                    if c_dict[key] == maxi:
                        answer.append(''.join(key))
    
    answer.sort()
    
    return answer