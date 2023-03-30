from bisect import bisect_right
for _ in range(int(input())):
    n = int(input())
    l = []
    for a in map(int, input().split()):
        i = bisect_right(l, a)
        if i == len(l):
            l.append(a); continue
        l[i] = a 
    print(len(l), *l)