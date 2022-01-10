'''
키패드 누르기
문제 요약
- 전화번호 키패드 0~9, *, # 있음
- input 값은 누를 번호 리스트와 왼손 or 오른손 잡이
- 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작한다.
- 1,4,7 왼손 입력
- 3, 6, 9 오른손 입력
- 0, 2, 5, 8 은 가까운 손 기준으로 입력 하지만 거리가 같으면 주 손잡이 기준으로 입력 한다.
- Output으로 입력한  왼손 엄지 손가락, 오른손 엄지손락 입력 순서대로 출력한다.

풀이
- 처음 왼손 엄지 손가락, 오른쪽 손가락 (x, y) 위치 선택한다.
- 키패드 왼쪽은 왼손 엄지 손가락 출력 하고 오른쪽은 오른손 손가라 출력한다.
- 출력한 다음 키패드 위치를 저장한다.
- 중간일 경우 거리를 계산 한다.(피타고라스 삼각함수 XXX), 거리에 따라 상황에 맞게 출력한다.
- 피타고라스 삼각함수 공식 사용 하면  누룰 수가 8인데 왼손 위치가 4 오른손 위치가 8일 경우
  거리는 2라서 주 손가락 기준으로 출력 해야 하는데 4가 더 우세 한다.

'''

# 거리 구하는 공식(피타고라스 X, 그냥 x축 차이와 , y축 차이를 계산해서 더한다.)
distance = lambda a, b: abs(a[0] - b[0])  + abs(a[1] - b[1])

def solution(numbers, hand):
    
    # 초기 세팅
    answer = ''
    L = (3, 0) # 왼손 엄지 손가락 위치
    R = (3, 2) # 오른손 엄지 손가락 위치
    
    # 키패드 위치 변수
    leftPad = [1, 4, 7] 
    midlePad = [2, 5, 8, 0]
    rightPad = [3, 6, 9]
    
    for number in numbers:
        if number in leftPad: # 왼쪽 패드 일경우
            answer += 'L'
            L = (leftPad.index(number), 0) # 누룬뒤 왼손 엄지손가락 위치 저장한다.
        elif number in midlePad: # 중간일 경우
            midleIndex = midlePad.index(number) # 키패드 중간 누룰 위치를 가져온다.
            # 양손 손가락과 누룰 위치랑 각각 계산한다.
            Ldistance = distance(L, (midleIndex, 1)) 
            Rdistance = distance(R, (midleIndex, 1))
            
            if Ldistance == Rdistance: # 거리가 같을 경우 주 손가락 우선으로 입력한다.
                if hand == 'right':
                    answer += 'R'
                    R = (midleIndex, 1)
                else:
                    answer += 'L'
                    L = (midleIndex, 1)
            elif Ldistance < Rdistance: # 가까운 손가락 입력한다.
                answer += 'L'
                L = (midleIndex, 1)
            else:
                answer += 'R'
                R = (midleIndex, 1)                            
        else: 
            answer += 'R'
            R = (rightPad.index(number), 2)
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))


'''
후기
처음에는 1차원 배열로 저장해서 계산해서 틀렸다.
2번째는 피타고라스 삼각함수 공식 사용 해서 거리 계산해서 틀렸다.
3번째에 맞췄다.
이 문제는 생각을 2번 더해야 맞출수 있다고 생각한다.
'''