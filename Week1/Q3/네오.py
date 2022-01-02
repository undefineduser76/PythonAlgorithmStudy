"""
문자열을 다루는 문제입니다.

0부터 9까지의 문자열을 저장해놓고
주어진 s에서 숫자에 해당하는 문자열을
정규식을 이용해서 치환하였습니다.

solution2 는 정규식을 사용하지 않는 풀이입니다.
"""


import re


def solution(s):
    num_to_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # 0~9까지 돌면서 문자열을 해당 숫자로 치환합니다.
    for i, num in enumerate(num_to_str):
        s = re.sub(num, str(i), s)

    return int(s)



def solution2(s):
    str_to_num = {
        "zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
        "six": '6', "seven": '7', "eight": '8', "nine": '9'
    }

    # bucket 은 임시적으로 추가된 영단어입니다.
    bucket = ""
    answer = ""

    # 문자열 s의 글자 c를 살핍니다.
    for c in s:
        # c가 알파벳이라면 영단어입니다.
        if str.isalpha(c):
            bucket += c

            # bucket 이 숫자에 해당하는 영단어라면 해당 영단어가 가리키는 숫자를 정답에 추가합니다.
            if bucket in str_to_num.keys():
                answer += str_to_num[bucket]
                # bucket 을 비웁니다.
                bucket = ""
        else:
            # c가 숫자라면 정답에 그대로 추가하고 bucket 을 비웁니다.
            answer += c
            bucket = ""

    return int(answer)


s = "one4seveneight"
print(solution2(s))
