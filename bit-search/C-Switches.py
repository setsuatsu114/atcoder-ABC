N, M = map(int, input().split())
switches = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))
ans = 0
# bit full search
for i in range(2**N):
    # スイッチの[on, off]パターンを決定
    on_off = [True]*N
    for j in range(N):
        if ((i >> j) & 1):
            on_off[j] = False
    
    # 幾つの電球が点灯するのか調べる
    ok = 0
    for m in range(M):
        cnt = 0
        for l in range(1, switches[m][0]+1):
            if on_off[switches[m][l]-1]:
                cnt += 1
        if cnt%2 == P[m]:
            ok += 1
    if ok == M:
        ans += 1

print(ans)