# 체육복

def solution(n, lost, reserve): # (전체학생수, 도난당한학생번호, 여벌가져온학생번호)
    lost.sort()
    reserve.sort()

    losty = lost.copy()
    lucky = [] # 체육복을 새로 얻게 된 학생 리스트

    for i in losty:
        # 체육복을 잃어버린 학생의 번호가 여벌을 가져온 학생 중에 있을 때
        if i in reserve:
            # 공통된 번호 삭제
            reserve.remove(i)
            lost.remove(i)

    for i in lost: 
        # 체육복을 잃어버린 학생의 앞번호 학생이 여벌을 가져왔을 때
        if i-1 in reserve:
            # 여벌을 가져온 학생의 체육복은 없어짐
            reserve.remove(i-1)
            # 체육복을 잃어버렸다가 생긴 학생의 번호 추가
            lucky.append(i)
        
        # 체육복을 잃어버린 학생의 뒷번호 학생이 여벌을 가져왔을 때
        elif i+1 in reserve:
            reserve.remove(i+1)
            lucky.append(i)
    
    # 체육수업 들을 수 있는 학생 수 = 전체학생 수 - 체육복 잃어버린 학생 수 + 체육복을 얻게 된 학생 수
    pe_students = n - len(lost) + len(lucky)  

    return pe_students