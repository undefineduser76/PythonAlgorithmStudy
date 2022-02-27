def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1

print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))