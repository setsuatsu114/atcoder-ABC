N = int(input())
A = list(map(int, input().split()))
ans = 2**30
for i in range(2**(N-1)):
    ored = 0
    xored = 0
    for j in range(N+1):
        if j < N:
            ored |= A[j] 
        if (j==N) or ((i >> j) & 1):
            xored ^= ored
            ored = 0
    # print('xored',xored)
    # print('ans', ans)
    ans = min(ans, xored)
print(ans)