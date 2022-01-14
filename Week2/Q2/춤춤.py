# 오픈채팅방
'''
입출력 예
record = ["Enter uid1234 Muzi", # uid1234가 Muzi로 들어옴
          "Enter uid4567 Prodo", # uid4567이 Prodo로 들어옴
          "Leave uid1234", # uid1234가 나감
          "Enter uid1234 Prodo", # uid1234가 Prodo로 들어옴
          "Change uid4567 Ryan"] uid4567이 Ryan으로 닉네임을 바꿈

result = ["Prodo님이 들어왔습니다.", 
          "Ryan님이 들어왔습니다.", 
          "Prodo님이 나갔습니다.", 
          "Prodo님이 들어왔습니다."]
'''
def solution(record):

    # 유저 고유의 아이디와 닉네임을 저장할 딕셔너리
    user = dict()

    # 오픈채팅방에 표시되는 결과
    result = []

    # 기록을 순회
    for i in range(len(record)):

        # 입력을 띄어쓰기로 구분 후 나갔을 때는 상태와 id만 표현되고 길이가 다르기 때문에 "Leave"만 제외
        if record[i].split(" ")[0] != "Leave":

            # "Enter"과 "Change"에 대해 user 딕셔너리에 id와 닉네임을 저장
            # 밖에서 변경하고 들어온 것과 내부에서 변경한 것을 같은 것으로 처리
            user['{0}'.format(record[i].split(" ")[1])] = '{0}'.format(record[i].split(" ")[2])
        
    # 기록을 순회
    for i in range(len(record)):

        # 들어오고 나간 상태를 표시하기 위해 "Change"만 제외
        if record[i].split(" ")[0] != "Change":
            if record[i].split(" ")[0] == "Enter":
                result.append("{0}님이 들어왔습니다.".format(user.get(record[i].split(" ")[1])))
            else:
                result.append("{0}님이 나갔습니다.".format(user.get(record[i].split(" ")[1])))


    return result