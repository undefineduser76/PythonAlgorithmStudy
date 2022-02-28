import heapq


def solution(n, works):
    works_queue = [(-works[i], i) for i in range(len(works))]
    heapq.heapify(works_queue)
    cnt = 0

    while len(works_queue) > 0 and cnt < n:
        w, wi = heapq.heappop(works_queue)

        if w < 0:
            w = -w - 1
            works[wi] = w
            heapq.heappush(works_queue, (-w, wi))
            cnt += 1

    answer = sum([w ** 2 for w in works])
    return answer
