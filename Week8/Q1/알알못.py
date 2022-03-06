def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes�� ������ ���� ���� (����) �������� ����
    camera = -30001 # -30001���� ī�޶� ��ġ�� ã���ϴ�.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))