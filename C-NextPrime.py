# C-Next Prime--------------------------------------------

def next_prime(n):
    for p in range(n,10000+n):
        is_prime = [True for _ in range(n+1)]
        is_prime[0] = False
        for i in range(2, n+1):
            if is_prime[i]:
                j = 2
                while j*i <= n:
                    is_prime[j*i]=False
                    j+=1
        if is_prime[p]:
            table = [i for i in range(2,n+1) if is_prime[i]]
            return is_prime, table, n
        else:
            n+=1

X = int(input())
is_prime, table, ans = next_prime(X)
# print(is_prime)
# print(table)
print(ans)