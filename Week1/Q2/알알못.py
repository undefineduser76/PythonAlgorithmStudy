'''
크레인 인형뽑기 게임
1. 2차원 배열로 "5 x 5" 이상 "30 x 30"
2. 0은 빈칸, 나머지는 인형 모양 번호
3. 집고 난후 바구니 맨 위에 모양이랑 같으면 터트려서 사라지게 한다.
4. 터트리는 갯수를 구한다.

풀이
1. moves for 문을 돌린다.
2. 열에 기준으로 맨 위 부터 0이 아닐때 까지 내려간다.
3. 0이 아닌 데이터 만나면 바구니에 있는 인형이 있는 경우 맨위랑 비교 한다.
4. 맨 위랑 같을 경우 바구니 맨위 삭제 시키고 터트리는 갯수 2개 증가한다.
5. 없는 경우 리스트에 추가한다.
'''

def solution(board, moves):
    answer = 0
    store = []
    for num in moves:
        k = len(board)
        # 맨 위 부터 찾아간다. 없으면 그냥 끝!!!
        for i in range(0, k):
            # 모양을 찾을 경우 바구니 리스트 맨뒤 랑 비교
            if board[i][num-1]:
                value = board[i][num-1]
                board[i][num-1] = 0
                if store and store[-1] == value: # 갚이 같을 경우 터트리는 갯수 증가하고 맨 뒤에 데이터 삭제
                    answer += 2                    
                    store.pop()
                else: store.append(value) # 다른 경우 추가 한다.
                break # 밑에 데이터도 바구니에 담으면 안되서 break문으로 탈출~ 
                
    return answer

'''
후기
열 기준으로 아래로 내려 가는 식으로 for문 돌려서
로직 작성 하면 쉽다.
'''