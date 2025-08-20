N, M = map(int, input().split())

sum = 0
for i in range(N):
    A = list(map(int, input().split()))

if A.sum() <= M:
    print("Yes")
else:
    print("No")
