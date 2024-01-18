N = int(input())

count = 0
for i in range(1, N+1):
    string = str(i)
    for s in string:
        if s == '2':
            print(s)
            count += 1

print(count)