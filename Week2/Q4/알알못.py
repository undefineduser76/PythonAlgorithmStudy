'''
거리두기 확인하기
문제 요약
1.대기실은 5개이며, 각 대기실은 5x5 크기입니다.
2.거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
3.단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
4. 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

문제 풀이
1. 각 플레이스에서 각 위치를 탐색한다.
2. 사람을 찾을 경우 맨허튼 거리 이내를 탐색한다.
3. 맨허튼 거리 이내 사람 있는 경우 조건에 맞는지 확인한다.
3. 조건이 맞으면 다음 사람 찾아 내고 아닌 경우 break 문을 빠지고 지키지 않았다고 한다.

'''

def solution(places):
    answer = [];


    for p in places:

        #거리두기가 지켜지지 않음을 확인하면 바로 반복을 멈추기 위한 key
        key = False;
        nowArr = [];

        #이번 place를 nowArr에 담아줍니다.
        for n in p:
            nowArr.append(list(n));
            
        for i in range(5):
            if key:
                break;

            for j in range(5):
                if key:
                    break;

                #사람을 찾아내면 판단을 시작합니다.
                if nowArr[i][j] == "P":

                    if i+1<5:
                        #만약 바로 아랫부분에 사람이 존재하면 break
                        if nowArr[i+1][j] == "P":
                            key = True;
                            break;
                        #만약 아랫부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i+1][j] == "O":
                            if i+2<5:
                                if nowArr[i+2][j] == "P":
                                    key = True;
                                    break;
                    #바로 오른쪽 부분에 사람이 존재하면 break    
                    if j+1<5:
                        if nowArr[i][j+1] == "P":
                            key = True;
                            break;
                            #만약 오른쪽 부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break   
                        if nowArr[i][j+1] == "O":
                            if j+2<5:
                                if nowArr[i][j+2] == "P":
                                    key = True;
                                    break;
                    #우측 아래 부분입니다.
                    if i+1<5 and j+1<5:
                        #만약 우측 아래가 사람이고, 오른 쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i+1][j+1] == "P" and (nowArr[i+1][j] == "O" or nowArr[i][j+1] == "O"):
                            key = True;
                            break;

                    #좌측 아래부분입니다.
                    if i+1<5 and j-1>=0:
                        #만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i+1][j-1] == "P" and (nowArr[i+1][j] == "O" or nowArr[i][j-1] == "O"):
                            key = True;
                            break;

        #위의 for문동안 key가 True로 변경되었다면 거리두가기 지켜지지 않은것 이므로 0을 answer에 추가
        if key:
            answer.append(0);
        else:
        #key가 false로 끝났다면 거리두기가 지켜졌으므로 1 추가
            answer.append(1);
    return answer        
