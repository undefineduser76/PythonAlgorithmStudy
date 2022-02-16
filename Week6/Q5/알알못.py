def solution(distance, rocks, n):
    position = [0] + sorted(rocks) + [distance] # [0, 2, 11, 14, 17, 21, 25]
    start = 1
    end = distance

    while start < end:
        mid = (start+end) // 2
        cnt = 0
        i = 0
        j = 1
        while j <= len(position)-1 :
            if position[j]-position[i] < mid:
                cnt += 1
                j += 1
            else:
                i = j
                j += 1
        if cnt > n:
            end = mid
        else:
            start = mid + 1
    return start - 1