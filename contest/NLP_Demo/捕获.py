def max_enemies(enemies, A, B):
    enemies.sort(key=lambda x: x[0]) # 按照x坐标从小到大排序
    n = len(enemies)
    ans = 0
    for i in range(n):
        j = i
        x, y = enemies[i][0], enemies[i][1]
        while j < n:
            x = max(x, enemies[j][0])
            y = min(y, enemies[j][1])
            if x- enemies[i][0] <= A and enemies[j][0] - x <= A and y - enemies[i][1] <= B and enemies[j][1] -y <= B:
                j += 1
            else:
                break
        ans = max(ans, j-1)
    return ans

N, A, B = map(int, input().split())
data = []
if 1<=N<=500 and 1<=A<= 1000 and 1<=B<= 1000:
    for i in range(N):
        t = tuple(map(int, input().split()))
        if 1<=t[0]<=1000 and 1<=t[1]<=1000:
            data.append(t)

print(max_enemies(data, A, B))
