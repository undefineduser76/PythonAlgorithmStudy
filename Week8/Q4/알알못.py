def solution(stones, k): 
    answer = 0 
    start, end = min(stones), max(stones) # 이진 탐색 
    while start <= end: 
        m = (start + end) // 2 # 한 번에 건너야 하는 디딤돌의 개수 중 최댓값 
        n, max_jump = 1, 0 
        for s in stones: 
            if s - m >= 0: 
                max_jump = max(n, max_jump) 
                n = 1 
            else: # 디딤돌을 밟지 못하는 경우 
                n += 1 
                max_jump = max(n, max_jump) # m명의 사람이 건널 수 없는 경우 
                if max_jump > k: 
                    end = m - 1 # m명의 사람이 건널 수 있는 경우 
                else: 
                    start = m + 1 
                    answer = max(answer, m) 
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))