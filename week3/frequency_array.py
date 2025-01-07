
n,m = map(int,input().split())


values = list(map(int,input().split()))

frq = [0] * (m+1)

for i in values:
    if 1 <= i <= m:
        frq[i] += 1


for i in range(1,m+1):
    print(frq[i])
