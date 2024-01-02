N = int(input())
X = list(map(int, input().split()))
# 素数
def sieve(n):
    a = [True for _ in range(n+1)]
    a[0] = False
    for i in range(2,n+1):
        if a[i]==True:
            j = 2
            while i*j <= n:
                a[i*j]=False
                j += 1
    b = [i for i in range(2, n+1) if a[i]]
    return b

from math import gcd
prime = sieve(50)
# bit full search
ans = []
for i in range(1,2**15):
    mul = 1
    for j in range(15):
        if ((i >> j) & 1):
            mul *= prime[j]
    gcds = []
    for x in X:
        gcds.append(gcd(mul, x))

    if all(gcdi != 1 for gcdi in gcds):
        ans.append(mul)

print(min(ans))