"""
큰 맥락은 다음과 같습니다.
1. {영단어:숫자} 에 대한 딕셔너리를 정의합니다.
2. 주어진 문자열에서 영어단어와 숫자에 해당하는 부분을 판별합니다.
    <고려할 것>
    i. 영어단어의 끝은 숫자를 만나기 전 또는 문자열의 마지막
    ii. 영어단어가 2개 이상 붙어있는 경우
3. 단어를 딕셔너리를 통해 숫자로 변환합니다.
"""

# 숫자에 대한 딕셔너리를 정의했습니다.
dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
       'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# 하나의 문자에 대해 숫자인지 판별하는 함수입니다.
def is_num(ch):
    # 숫자 0~9까지 아스키코드 값: 48~57
    if 48 <= ord(ch) <= 57:
        return True
    else:
        return False

# 영어단어를 숫자로 바꿔주는 함수입니다.
def word2num(word):
    # 만약 단어가 딕셔너리에 있는 단어라면 그에 해당하는 숫자를 반환합니다.
    if word in dic:
        return dic[word]
    # 만약 단어가 딕셔너리에 없는 단어라면
    # 다시말해, seveneight 처럼 여러개가 붙어있는 붙어있는 단어라면
    else:
        # 단어의 처음부터 끝까지 순회하면서
        for i in range(len(word)):
            # word[:i]가 딕셔너리에 있는 단어인지 찾습니다.
            # 예) s, se, sev, seve 이렇게 보다가
            # i=5, seven이 된 경우 딕셔너리에 있으므로
            if word[:i] in dic:
                # seven을 숫자로 바꾸고 + 나머지 문자열에 대해 똑같은 방식으로 처리합니다.
                return dic[word[:i]] + word2num(word[i:])

def solution(s):
    # 정답을 위해 숫자를 하나씩 이어붙일 변수입니다.
    answer = ""
    # 숫자가 아닌 경우 문자를 임시 이어붙일 변수입니다.
    word = ""

    # 주어진 문자열의 각 문자를 순회합니다.
    for ch in s:
        # 숫자인 경우
        if is_num(ch):
            if word:
                # 단어가 비어있지 않다면 숫자로 변환해서 정답에 이어붙이고
                # 단어 변수를 비워줍니다.
                answer += word2num(word)
                word = ""
            # 숫자를 정답에 이어붙입니다.
            answer += ch

        # 알파벳인 경우
        # word 변수에 붙여줍니다.
        else:
            word += ch

    # 주어진 문자열을 다 순회하고 나서 단어가 비어있지 않은 경우
    # 숫자로 변환 후 정답에 이어 붙입니다.
    if word:
        answer += word2num(word)

    # answer 변수에는 문자열이 담겨있기 때문에 정수로 바꿔줍니다.
    return int(answer)

s = "fourfivesixseven"
print(solution(s))