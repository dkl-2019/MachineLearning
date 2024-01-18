from collections import defaultdict

def dfs(u, fa, d):
    dist[u] = d


n = int(input())
graph = defaultdict(list)
dist = [0] * (n+1)
energy = [0] * (n+1)

weight = []
for i in range(1, n+1):
    weight[i] = int(input())

for i in range(n-1):
    u ,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)