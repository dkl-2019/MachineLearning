N, X, Y = map(int, input().split())
goods = []
for _ in range(N):
    p, d = map(int, input().split())
    goods.append((p-d, p))
goods.sort()
cost = 0
cnt = 0
for i in range(N):
    if i < Y:
        cost += min(goods[i])
    else:
        cost += goods[i][1]
    if cost > X:
        break
    cnt += 1
print(cnt,cost)