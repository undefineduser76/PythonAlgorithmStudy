'''
숫자 문자열과 영단어
-숫자 영어와 숫자 썩인 문자열을 숫자로 변환한다. 

풀이
1. 딕셔너리 사용해서 단어와 숫자 key value로 설정한다.
2. 문자열에 있는 문자 하나씩 들고 온다.
3. 문자가 숫자 이면 뒤에 숫자 붙인다.
4. 알파벳이면 단어가 완성 될때까지 문자열을 붙이고 key 맵핑되어 있는 숫자를 가져온다.
'''

# 단어와 숫자 설정한다.
key = {
'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4 , 
'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
}

def solution(s):
    answer = 0
    number = '' # 단어 변수
    # 문자하나씩 가져온다.
    for char in s:     
        number += char
    
        # 완성된 단어나 숫자인경우 뒤에 붙이고 number 변수 초기화 한다.
        if number.isdigit():
            answer = answer *10 + int(number)
            number = ''
        elif number in key.keys():
            answer = answer *10 +key[number]
            number = ''
        
    return answer