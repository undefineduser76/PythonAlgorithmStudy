# 키패드 누르기
'''
입출력 예제
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''

def solution(numbers, hand):
    answer = ''

    # 번호별 좌표 딕셔너리
    xy = {1:[0,0], 2:[0,1], 3:[0,2],
          4:[1,0], 5:[1,1], 6:[1,2],
          7:[2,0], 8:[2,1], 9:[2,2],
          '*':[3,0], 0:[3,1], '#':[3,2]}
    
    # 현재 손의 위치
    finger = {'L':xy['*'], 'R':xy['#']}
    
    for n in numbers:

        # 1,4,7일 때 왼손 L 추가
        if n in [1,4,7]:
            answer += 'L'
            finger['L'] = xy[n]

        # 3,6,9일 때 오른손 R 추가
        elif n in [3,6,9]:
            answer += 'R'
            finger['R'] = xy[n]

        # 2,5,8,0일 때
        else:
            # 왼손, 오른손 거리 계산
            L_d = 0
            R_d = 0

            # 이전 왼손위치, 이전 오른손위치와 현재 번호 위치 간 거리 계산
            for l,r,d in zip(finger['L'], finger['R'], xy[n]):
                L_d += abs(l-d)
                R_d += abs(r-d)

            # 왼손과의 거리가 더 짧으면 왼손
            if L_d < R_d:
                answer += 'L'
                finger['L'] = xy[n]

            # 오른손과의 거리가 더 짧으면 오른손
            elif R_d < L_d:
                answer += 'R'
                finger['R'] = xy[n]

            # 거리가 같으면 왼손잡이/오른손잡이에 따라 움직임
            else:
                if hand == 'left':
                    answer += 'L'
                    finger['L'] = xy[n]
                else:
                    answer += 'R'
                    finger['R'] = xy[n]

    return answer