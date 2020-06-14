from collections import defaultdict

n, m = list(map(int, input().split()))
a = defaultdict(list)

for i in range(1, n + 1):
    palavra_a = input()
    a[palavra_a].append(i)

for i in range(m):
    palavra_b = input()
    if palavra_b in a:
        print(*a[palavra_b])
    else:
        print(-1)
