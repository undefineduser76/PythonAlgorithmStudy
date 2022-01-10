'''
오픈 채팅방
문제 요약
- "[닉네임]님이 들어왔습니다.",  "[닉네임]님이 나갔습니다." 출력
- 닉네임 변경 방법 두가지
1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
2. 채팅방에서 닉네임을 변경한다.
- 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 한다.

문제 풀이
1. 아이디 : 닉네임 key value 저장할 변수 선언
2. 최종적으로 변경된 닉네임 기준으로 봐야 해서 저장 할때 아이디와 들어왔다 나갔다만 추가한다.
3. Enter 일때 dic타입에 저장하고 id 와 들어왔다고 추가한다.
4. Leave 일때 id와 나갔다고 저장한다.
5. Chnage 키값의 이름 값만 변경한다.
6. 최종적으로 id로 저장 한것을 닉네임 변경 작업한다.

'''

user = {} #dic Type 변수 선언

def solution(record):
    answer = []
    for data in record:
        infor = data.split() # 띄어쓰기 기준으로 리스트로 만든다.
        if infor[0] == 'Enter': # 들어 갈때
            user[infor[1]] = infor[2] # 키값 과 이름 저장한다.
            answer.append((infor[1], 'E'))  # ID와 들어 갔다고 표시한다.
        elif infor[0] == 'Leave': # 나갈때
            answer.append((infor[1], 'L')) # ID와 나갔다고 표시한다.
        elif infor[0] == 'Change': # 닉네임 변경 할때
            user[infor[1]] = infor[2]
            
    # 순차적으로 기록한것을 id → 닉네임, 행위 코드 값을 행위로 변경한다.           
    return [user[data[0]] + ('님이 들어왔습니다.' if data[1] == 'E' else '님이 나갔습니다.') for data in answer]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))