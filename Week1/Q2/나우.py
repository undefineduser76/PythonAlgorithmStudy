board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stack = [] # 뽑은 인형을 담을 스택 변수입니다.
    for mv in moves:
        for i in range(len(board)):
            # 현재 뽑힌 인형에 대해 cur 변수에 저장합니다.
            cur = board[i][mv - 1]

            # 뽑힌 인형이 0이 아닌 경우
            if cur != 0:
                # 뽑힌 위치를 0으로 바꿔줍니다.
                board[i][mv - 1] = 0
                # 만약 스택이 비어있지 않고, 스택의 마지막 인형이 현재 뽑은 인형과 같다면
                if stack and stack[-1] == cur:
                    # 스택의 마지막 원소를 없애고 정답을 2개 늘려줍니다.
                    stack.pop()
                    answer += 2
                # 스택의 마지막 인형이 현재 뽑은 인형과 다르다면
                # 스택에 넣어줍니다.
                else:
                    stack.append(cur)
                break
    return answer

print(solution(board, moves))