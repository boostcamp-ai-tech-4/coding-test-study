#21317_징검다리건너기.py
import sys
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n-1)]
k = int(input())

# n이 짧을때에 대해 예외처리
if n ==1:
    print(0)
    sys.exit()
if n ==2:
    print(lst[0][0])
    sys.exit()
if n ==3:
    print(min(lst[0][1],lst[0][0]+lst[1][0]))
    sys.exit()


dp = [[10**10] * n for _ in range(n-2)]
dp[0][0] = 0


#1,2 만으로 일반적인 dp[0] 갱신
for jump in [1,2]:
    for i in range(jump,n):
        dp[0][i] = min(dp[0][i-jump] + lst[i-jump][jump-1], dp[0][i])

answer = dp[0][-1]

#슈퍼 점프 할 수 있는 위치별로 한번씩 dp 갱신
for j in range(n-3):
    #슈퍼 점프 전까지는 기존 DP 복사, 슈퍼점프 위치까진 갱신
    dp[1+j][:j+1] = dp[0][:j+1]
    dp[1+j][j+3] = dp[1+j][j] + k
    #슈퍼 점프 이후에 1,2 점프로 갱신
    for jump in [1,2]:
        for i in range(jump + 3,n):
            dp[1+j][i] = min(dp[1+j][i-jump] + lst[i-jump][jump-1], dp[1+j][i])
    answer = min(answer,dp[1+j][-1])
print(answer)

# 예시 인풋에 대해 dp가 아래와 같이 갱신 되는데 틀리는 이유를 모르겠음...
#[[0, 1, 2, 4, 7],
# [0, 10000000000, 10000000000, 4, 10],
# [0, 1, 10000000000, 10000000000, 5]]