def is_wedge_number(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factorize(n):
        f = 2
        a = []
        while n%f==0:
            a.append(f)
            n//=f
        f = 3
        while is_prime(f):
            if n%f==0:
                a.append(f)
                n//=f
            else:
                f+=2
            if n==1:
                return a

    if n < 30:
        return False

    prime_factors = prime_factorize(n)
    
    # 異なる素数が3つ以上あるかどうかを判定
    unique_prime_factors = set(prime_factors)
    return len(unique_prime_factors) >= 3

# 例: 30は楔数である
# example_number1 = 30
N = int(input())
ans = 0
for i in range(30, N+1):
    print(i, is_wedge_number(i))
    if is_wedge_number(i):
        ans+=1
print(ans)  # 出力: True

# 例: 25は楔数でない
# example_number2 = 25
# result2 = is_wedge_number(example_number2)
# print(result2)  # 出力: False
