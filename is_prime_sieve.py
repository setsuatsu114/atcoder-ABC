N = int(input())

# エラトステネスのふるい
def is_prime(n):
    if n==1:
        return 0, [n]
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    for i in range(2, n+1):
        if is_prime[i]:
            j = 2
            while j*i <= n:
                is_prime[j*i]=False
                j+=1
    table = [i for i in range(2, n+1) if is_prime[i]]
    return is_prime, table

is_prime, table = is_prime(N)
# print('is_prime', is_prime)
# print(table)
print(len(table)-1) if table[-1]==N else print(len(table))