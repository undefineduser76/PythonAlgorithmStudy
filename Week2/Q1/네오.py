def solution(numbers, hand):
    answer = ''
    finger = {"left": '*',
              "right": '#'}

    get_keypad()

    for n in numbers:
        if is_left(n):
            used = 'left'
        elif is_right(n):
            used = 'right'
        else:
            dist_l = get_distance(finger['left'], n)
            dist_r = get_distance(finger['right'], n)
            if dist_l < dist_r:
                used = 'left'
            elif dist_l == dist_r:
                used = hand
            else:
                used = 'right'
        finger[used] = n
        answer += used[0].upper()

    return answer


def get_keypad():
    global keypad
    keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    keypad = {}

    for i in range(4):
        for j in range(3):
            keypad[keys[i][j]] = (i, j)


def is_left(key):
    return key in [1, 4, 7]


def is_right(key):
    return key in [3, 6, 9]


def get_distance(_from, _to):
    p1 = keypad[_from]
    p2 = keypad[_to]
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
