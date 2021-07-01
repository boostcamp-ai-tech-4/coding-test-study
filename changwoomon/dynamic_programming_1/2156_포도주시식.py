###### 2156번: 포도주 시식
# https://www.acmicpc.net/problem/2156
# 메모리/시간: 32568KB / 96ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

wine = [int(input()) for _ in range(n)]
table = defaultdict(int)

table[0] = wine[0]

for i in range(1, n):
    table[i] = max(table[i-1], wine[i]+table[i-2], wine[i]+wine[i-1]+table[i-3])

print(table[n-1])