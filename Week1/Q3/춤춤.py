# 숫자 문자열과 영단어

def solution(s):
    # 문자열과 숫자값을 가진 딕셔너리 생성
    match = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
             "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    
    for key in match:

        # 만약 문자열 내에 해당 키가 있을 때
        if key in s: 

            # 해당 문자열을 키로 가진 딕셔너리의 값으로 변경
            s = s.replace(key, str(match.get(key)))

    # 문자형을 정수형으로 변경
    answer = int(s)
    return answer