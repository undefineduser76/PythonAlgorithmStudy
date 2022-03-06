def solution(stones, k): 
    answer = 0 
    start, end = min(stones), max(stones) # ���� Ž�� 
    while start <= end: 
        m = (start + end) // 2 # �� ���� �ǳʾ� �ϴ� ������� ���� �� �ִ� 
        n, max_jump = 1, 0 
        for s in stones: 
            if s - m >= 0: 
                max_jump = max(n, max_jump) 
                n = 1 
            else: # ������� ���� ���ϴ� ��� 
                n += 1 
                max_jump = max(n, max_jump) # m���� ����� �ǳ� �� ���� ��� 
                if max_jump > k: 
                    end = m - 1 # m���� ����� �ǳ� �� �ִ� ��� 
                else: 
                    start = m + 1 
                    answer = max(answer, m) 
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))