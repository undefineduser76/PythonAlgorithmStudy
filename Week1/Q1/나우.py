# n, lost, reserve = 5, [2, 4], [1, 3, 5] # 5
# n, lost, reserve = 5, [2, 4], [3] # 4
# n, lost, reserve = 3, [3], [1] # 2
# n, lost, reserve = 10, [4,6], [3,5] # 10
n, lost, reserve = 10, [4,6], [5,3] # 10 # 정렬 안하는 경우 return 9

def solution(n, lost, reserve):
    # 여벌옷이 있는데 도난을 당한 학생은 아예 제외하고 시작합니다.
    # 교집합을 제거하는 방식으로 구현했습니다.
    intersection = list(set(lost) & set(reserve))
    for ele in intersection:
        reserve.remove(ele)
        lost.remove(ele)

    # 각 배열을 정렬해줍니다. (정렬하는 이유는 맨 밑 회고에 있습니다.)
    lost.sort()
    reserve.sort()

    # 학생들의 체육복 유무를 나타내는 변수입니다.
    clothes = [1] * n

    # 도난당한 학생들에 대해 체육복 소지 여부를 0으로 업데이트 합니다.
    for i in lost:
        clothes[i-1] = 0

    # 빌려줄 수 있는 학생들을 순회하면서
    for i in reserve:
        # 앞 학생의 인덱스가 유효하고 체육복이 없다면
        # 앞 학생의 체육복 소지 여부를 1로 바꿔줍니다.
        # 체육복을 빌려줬다면 더이상의 조건은 확인하지 않고
        # 다음 학생으로 넘어갑니다.
        if i-2 >= 0 and clothes[i-2] == 0:
            clothes[i-2] = 1
            continue

        # 뒤 학생의 인덱스가 유효하고 체육복이 없다면
        # 뒤 학생의 체육복 소지 여부를 1로 바꿔줍니다.
        elif i < n and clothes[i] == 0:
            clothes[i] = 1

    # 옷을 가진 (1) 학생 수를 세서 반환합니다.
    return clothes.count(1)

print(solution(n, lost, reserve))

"""
<회고>
- 처음 짠 코드에서는 첫번째 if문에서 부등호 실수를 해서 테스트케이스 11, 13-16을 통과하지 못했다. (부등호 '>' 에서 '>=' 로 바꿈)
배열의 인덱스 자체는 0 <= idx < n 인데 여기서 i-2를 가지고 생각하느라 잠시 헷갈렸던 것 같다.

- 저걸 해결하고 나서는 아무리 해도 테케 18, 20이 해결되지 않았다.
검색 끝에 lost와 reserve 배열을 정렬해줘야 한다는 것을 알았고, 그 이유는 다음과 같다.
이 문제는 '최대한' 많은 학생이 체육수업을 들을 수 있도록 해야하는데 정렬하지 않으면 다음과 같은 문제가 발생한다.

(아래 글 출처: https://ongveloper.tistory.com/90)
만약 4번 학생과 6번 학생이 체육복을 잃어버렸고,
3번 학생과 5번 학생이 여벌의 체육복을 가지고 있다고 하자.
4번 학생이 5번 학생에게 체육복을 빌린다면 6번 학생은 체육복을 입지 못하고,
4번 학생이 3번 학생에게 체육복을 빌린다면 6번 학생은 5번 학생에게 체육복을 빌릴 수 있다.
따라서 lost와 reserve를 정렬하고, 앞에서부터 짝을 지어준다.
"""