# 순위 검색
'''
입출력 예시
info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
'''
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    f_dict = dict()

    for i in info:
        # 각 info에 대해 띄어쓰기를 기준으로 분리
        feature = i.split(' ') # ['java', 'backend', 'junior', 'pizza', '150']

        # 각 항목과 점수로 분리
        f_key = feature[0:-1] # ['java', 'backend', 'junior', 'pizza']
        f_val = int(feature[-1]) # 150

        for j in range(5):
            # info 항목에 대해 모든 조합을 생성
            for c in combinations(f_key, j): # ('java'), ('backend'), ('junior'), ('pizza'), ('java','backend'),...
                # 텍스트병합
                tmp = ''.join(c) # 'java', 'backedn', 'junior', 'pizza', 'javabackend',...

                # f_dict에 병합한 텍스트가 키로 있으면 해당하는 값에 점수를 원소로 추가, 없으면 새로운 키:값 생성
                if tmp in f_dict:
                    f_dict[tmp].append(f_val)
                else:
                    f_dict[tmp] = [f_val]

    # 점수 오름차순 정렬
    for f in f_dict:
        f_dict[f].sort()

    for q in query:
        # 각 query에 대해 띄어쓰기를 기준으로 분리
        qu = q.split(' ') # ['java', 'and', 'backend', 'and', 'junior', 'and', '100']

        # 각 항목과 점수로 분리
        q_key = qu[0:-1] # ['java', 'and', 'backend', 'and', 'junior', 'and']
        q_val = int(qu[-1]) # 100

        # '-'와 'and' 모두 삭제
        while '-' in q_key: 
            q_key.remove('-')
        while 'and' in q_key:
            q_key.remove('and')
        
        # 텍스트 병합
        q_key = ''.join(q_key) # 'javabackendjunior'

        # query에서 병합해 만든 항목이 f_dict에 있으면 score에 점수 추가
        if q_key in f_dict:
            score = f_dict[q_key] # [80, 150]

            # 점수가 들어갈 위치를 찾고 score의 길이에서 해당 숫자를 뺌
            enter = bisect_left(score, q_val) # 1
            answer.append(len(score) - enter) # 2-1 = 1

        # 그렇지 않으면 0
        else:
            answer.append(0)

    return answer