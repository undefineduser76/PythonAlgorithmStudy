def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)] # ������ ����� ���� �迭

    for type, r1, c1, r2, c2, degree in skill:
        # ������ ���, ��ȣ�� ������ ��
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # �� ���� ������
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    # �� ���� ������
    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    # ���� �迭�� ����
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            # board�� ���� 1�̻��� ��� answer++
            if board[i][j] > 0: answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))