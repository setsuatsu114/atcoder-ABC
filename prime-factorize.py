N = int(input())

def prime_factorize(n):
    f = 2
    a = []
    while n%f==0:
        a.append(f)
        n //= f
    print(a)
    i = 3
    while True:
        if n%i==0:
            a.append(i)
            n //= i
        else:
            i += 2
        if n==1:
            break
    return a
        
print(prime_factorize(N))
