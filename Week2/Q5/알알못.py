'''
순위 검색
문제 요약: 각 쿼리문에 맞는 정보가 몇개 있는지 가져온다.

품이
1. 단순하게 쿼리문 for문 데이터들을 for문 돌리면 정확성은 맞지만 효율성에서 떨어진다.
2. info 안의 문자열을 공백기준으로 리스트로 만든다.
3. 키값들로 만들 수 있는 모든 조합 만든다.
4. 조합으로 딕셔너리 만든다. 
5. 조합으로 만든것을 value에 추가한다.
6. 딕셔너리 각 원소마다 value 값들을 기준으로 정렬
7.  query를 한바퀴 돌면서, info딕셔너리를 탐방하게 되는데, query의 key값이 info딕셔너리의 키값으로 존재하면 그 info딕셔너리의 value값들을 온다.
8. 가져온 점수값에서 기준 점수값을 넘는 것들의 개수를 이분탐색을 통해 구하면 된다.
'''

from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer