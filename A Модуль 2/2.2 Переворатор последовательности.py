n, x, y, a, b = map(int, input().split())
l =[i for i in range(1, n + 1)]

l[x-1:y] = l[x-1:y][::-1]
l[a-1:b] = l[a-1:b][::-1]
print(*l)
