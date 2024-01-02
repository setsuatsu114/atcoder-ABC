N, M = map(int, input().split())
AB = [set(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]
condition_max = 0
for i in range(2**K):
    loop1 = []
    for j in range(K):
        if ((i>>j)&1):
            loop1.append(CD[j][0])
        else:
            loop1.append(CD[j][1])
    check1 = [0]*M
    loop1 = set(loop1)
    l = 0
    for ab in AB:
        if len(loop1.intersection(ab)) > 1:
            check1[l] = 1
        l += 1
    condition_max = max(condition_max, check1.count(1))
print(condition_max)
