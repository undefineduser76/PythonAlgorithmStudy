"""
문제가 설명하는 로직을 코드로 구현하는 문제입니다.
"""

def solution(board, moves):
    # 집어 올린 인형이 들어갈 바구니입니다.
    basket = []

    # 터뜨려져 사라진 인형의 개수입니다.
    answer = 0

    # board 의 세로 길이입니다.
    n = len(board)

    # 크레인을 j의 위치로 움직입니다. j는 board 의 열(column)에 해당합니다.
    for j in range(len(moves)):
        # moves 배열에서 숫자가 1부터 시작하므로 1을 빼줍니다.
        m = moves[j] - 1

        # 크레인을 위(i=0)에서부터 끝까지(i=n) 내립니다.
        for i in range(n):
            # 0이 아닌 값(인형)이 발견되었다면 인형을 바구니에 넣습니다.
            if board[i][m] != 0:
                # 바구니에 인형이 하나 이상 있으면서 맨 위의 인형과 지금 크레인이 집은 인형이 같다면
                # (= 새로 인형을 추가하면 그 인형이 2개가 연속되는 경우)
                if len(basket) > 0 and basket[-1] == board[i][m]:
                    # 바구니의 위에서 인형 하나를 버린 후 정답에 2를 더합니다.
                    basket.pop()
                    answer += 2
                else:
                    # 연속되지 않는다면 바구니에 인형을 추가합니다.
                    basket.append(board[i][m])

                # 인형의 위치를 빈 칸으로 표시합니다.
                board[i][m] = 0
                break
    
    return answer