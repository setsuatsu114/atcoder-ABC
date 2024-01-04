# 不正解あり

# 標準入力
N = int(input())
A, X = [], []
ans = 0
for i in range(N):
    a = int(input())
    A.append(a)
    x = [list(map(int, input().split())) for _ in range(a)]
    X.append(x)
for i in range(2**N):
    tf = [0 for _ in range(N)]
    for j in range(N):
        if ((i >> j) & 1):
            tf[j] = 1
# ビット全探索
    flag = False
    cnt = 0
    for k in range(N):
        for a in range(A[k]):
            if tf[k]==1 and X[k][a][1] != tf[X[k][a][0]-1]:
                flag = True
                break
            if tf[k]==0 and X[k][a][1] == tf[X[k][a][0]-1]:
                flag = True
                break
        if flag:
            break
        cnt += 1
    if cnt == N:
        ans = max(ans, tf.count(1))
print(ans)

