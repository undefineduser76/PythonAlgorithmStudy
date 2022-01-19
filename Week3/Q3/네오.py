"""
누적합 문제입니다.
타임스탬프를 배열의 인덱스로 바꾸고 다시 인덱스를 타임스탬프로 바꾸는 테크닉이 추가됩니다.
"""


def solution(play_time, adv_time, logs):
    time_seq = init_time_seq(play_time, logs)

    # 광고 길이
    adv_len = timestamp_to_idx(adv_time)
    n = 0
    max_watching = 0
    max_adv_start = 0
    watching = 0

    # 최초 구간합을 구합니다.
    for i in range(adv_len):
        n += time_seq[i]
        time_seq[i] = n
        watching += n

    i = 0
    while True:
        # 현재 구간에 대해서 최대값을 갱신하고, 갱신될 시 구간 시작값인 i를 저장합니다.
        if max_watching < watching:
            max_watching = watching
            max_adv_start = i

        if i >= len(time_seq) - adv_len:
            break

        # 앞값을 빼고 뒷값을 더합니다.
        n += time_seq[i + adv_len]
        time_seq[i + adv_len] = n
        watching -= time_seq[i]
        watching += n
        i += 1

    answer = idx_to_timestamp(max_adv_start)
    return answer


def timestamp_to_idx(timestamp):
    HH, MM, SS = map(int, timestamp.split(':'))
    return HH * 3600 + MM * 60 + SS


def idx_to_timestamp(idx):
    MM, SS = divmod(idx, 60)
    HH, MM = divmod(MM, 60)
    return "%02d:%02d:%02d" % (HH, MM, SS)


def init_time_seq(play_time, logs):
    # time_seq[i] 는 i 번을 지났을 때 더해나갈 값입니다.
    max_time = timestamp_to_idx(play_time)
    time_seq = [0 for _ in range(max_time + 1)]

    for log in logs:
        [from_, _to] = log.split('-')
        time_seq[timestamp_to_idx(from_)] += 1
        time_seq[timestamp_to_idx(_to)] -= 1

    return time_seq
