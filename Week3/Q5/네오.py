from itertools import permutations


def solution(n, weak, dist: list):
    all_dist_seq = list(permutations(dist, len(dist)))
    min_cnt = len(dist) + 1

    for i in range(len(weak)):
        for dist_seq in all_dist_seq:
            min_cnt = min(min_cnt, is_possible(n, weak, dist_seq, i))

    if min_cnt == len(dist) + 1:
        return -1
    return min_cnt


def is_possible(n, weak, dist_seq, next_to_fix):
    fixed_cnt = 0

    for i in range(len(dist_seq)):
        now_wall = weak[next_to_fix]

        for j in range(dist_seq[i] + 1):
            if weak[next_to_fix] == now_wall:
                next_to_fix = (next_to_fix + 1) % len(weak)
                fixed_cnt += 1

                if fixed_cnt == len(weak):
                    return i + 1

            now_wall = (now_wall + 1) % n

    return len(weak) + 1




n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))