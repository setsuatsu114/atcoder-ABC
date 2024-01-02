N = input()
N = [string for string in N]
digits = len(N) # 桁数
ans = []
# bit full search
for i in range(2**digits):
    multiple3 = []
    for j in range(digits):
        if ((i >> j)&1):
            multiple3.append(N[j])
    sum_ = 0
    sum_ = [int(n) for n in multiple3]
    if sum(sum_)%3==0:
        ans.append(multiple3)
        
ans = [len(s) for s in ans]
if not ans:
    print(-1)    
else:
    print(digits-max(ans))