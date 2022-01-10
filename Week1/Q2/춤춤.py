# 크레인 인형뽑기게임

def solution(board, moves):
    # 사라지는 인형의 개수
    doll = 0 
    # 인형이 담기는 배열
    bucket = []

    for j in moves: # 인형을 뽑는 위치를 반복
        for i in range(len(board)): # 맨 처음 행부터 아래 행까지 반복
            
            # 뽑으려는 위치(j-1)의 숫자가 0이 아니면
            if board[i][j-1] != 0:
                # 해당되는 인형 번호를 배열에 추가
                bucket.append(board[i][j-1])
                # 0으로 변경
                board[i][j-1] = 0
                # 더 이상 아래로 내려가지 않도록 반복문 탈출
                break
                
        # 담긴 배열의 길이가 2 이상이고, 마지막 담긴 인형의 번호와 그 전의 번호가 같으면
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            
            # 마지막 하나와 그 전 하나의 인형 번호를 뺌
            bucket.pop(-1)
            bucket.pop(-1)
            # 버린 인형 숫자에 2 추가
            doll += 2

    return doll