def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key=lambda x: x[1])

    for drive_in, drive_out in routes:
        if not (drive_in <= camera <= drive_out):
            answer += 1
            camera = drive_out

    return answer
