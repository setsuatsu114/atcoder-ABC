N = int(input())

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    for i in range(2, n+1):
        if is_prime[i]:
            j = 2
            while j*i<=n:
                is_prime[j*i] = False
                j+=1
    table = [i for i in range(2, n+1) if is_prime[i]]
    return table, is_prime

table, is_prime = sieve(N)
print(table)
print(is_prime)
