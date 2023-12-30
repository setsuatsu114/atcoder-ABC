# 素因数分解
def prime_factorize(n):
    a = []
    for t in table:
        while n%t==0:
            a.append(t)
            n//=t
        if len(a)>3:
            return [0]
    return a

# 2からNまでの素数を計算
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if is_prime[i]:
            j=2
            while j*i <= n:
                is_prime[i*j] = False
                j += 1
    table = [i for i in range(2,n+1) if is_prime[i]]
    return table
N = int(input())
table = sieve(N)
ans = 0
for i in range(30, N+1):
    prime_f = prime_factorize(i)
    if len(prime_f)==len(set(prime_f))==3:
        ans+=1
print(ans)


# N = int(input())
# ans = 0

# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a

# for i in range(1,N+1):
#     p = prime_factorize(i)
#     if len(p) == len(set(p)) and len(p) == 3:
#         ans += 1
# print(ans)