# https://www.acmicpc.net/problem/7569
import sys
from collections import deque

def bfs():
    global num_1
    q = deque(tomato)
    cnt = -1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            for d in directions:
                nk=node[0]+d[0]
                ni=node[1]+d[1]
                nj=node[2]+d[2]
                # 토마토가 익지 않았다면
                if tomato_box[nk][ni][nj] == 0:
                    tomato_box[nk][ni][nj] = 1  # 익히기
                    q.append((nk, ni, nj))  # 큐에 삽입
                    num_1+=1
        cnt += 1
    return cnt

input = sys.stdin.readline
directions=[[0,1,0],[-1,0,0],[1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]


# 입력
n, m, h = map(int, input().split())
tomato_box = [[[-1]*(n+2) for _ in range(m+2)]]
for _ in range(h):
    plane=[[-1]*(n+2)]
    for _ in range(m):
        line=list(map(int,input().split()))
        line.insert(0, -1)
        line.append(-1)
        plane.append(line)
    plane.append([-1]*(n+2))
    tomato_box.append(plane)
tomato_box.append([[-1]*(n+2) for _ in range(m+2)])
tomato=[]
is_raw = False  # 안익은 토마토가 있는지
flag=False   # 토마토가 다 익을지
num_1=0   # 익은 토마토 수
num_m1=0  # 토마토가 들어있지 않는 수
for k in range(1,h+1):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if tomato_box[k][i][j]==0 and not flag:  # 토마토가 다 익을지 확인 and 안익은 토마토면
                is_raw=True  # 안익은 토마토가 있으니 True로 바꿔줌
                flag=True    # 토마토가 안 익을꺼라고 가정
                for d in directions: # 4방향 탐색으로 고립된 토마토인지 확인  주의 할점: [1,0,-1] [0,-1,0] [-1,0,0] 일때처럼 외딴섬 문제 처럼 되어있으면  못잡아냄
                    if tomato_box[k][i+d[0]][j+d[1]]!=-1:
                        flag=False # 한방향이라도 -1이 아니면 False로 바꿈
            elif tomato_box[k][i][j]==1:
                tomato.append([k,i,j]) # 탐색할 토마토 위치 잡아주기
                num_1+=1 # 익은 토마토 개수 ++
            elif tomato_box[k][i][j]==-1:
                num_m1+=1 # 안익은 토마토 개수 ++

if flag: # 토마토가 안익을거 같으면 -1
    print(-1)
else:
    if is_raw: # 익을 토마토가 있으면
        ans=bfs()
        if n*m*h==(num_1+num_m1): # 전체 칸수랑 익은 토마토개수 + 안익은 토마토 개수가 다르면 안익은 토마토가 있다는거니 -1 출력
            print(ans)
        else:
            print(-1)
    else: # 이미 토마토가 다익음
        print(0)