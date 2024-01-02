# dic = {}
# dic["orange"] = 100
# dic["apple"] = 200
# dic["grape"] = 300
# print(dic)
# keys = list(dic.keys())
# n = len(dic)
# for i in range(2**n):
#     bag = []
#     print("pattern {}:".format(i), end="")
#     for j in range(n):
#         print(i>>j)
#         if ((i >> j) & 1):
#             bag.append(keys[j])
#     print(bag)
import numpy as np
N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
ans = []
for i in range(2**N):
    understands = np.zeros(M)
    money = 0
    for j in range(N):
        if ((i >> j) & 1):
            money += CA[j][0]
            understands[:] += CA[j][1:]
    # print('money',money)
    # print('rikaido',understands)
    if all(understand >= X for understand in understands):
        ans.append(money)
        # print('clear')

print(-1) if not ans else print((min(ans)))