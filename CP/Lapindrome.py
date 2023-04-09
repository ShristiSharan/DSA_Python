import math
T=int(input())
for i in range(T):
    S=str(input())
    l=len(S)
    if l%2==0:
        p=int(l/2)
        if sorted(S[:p])==sorted(S[p:]):
            print("YES")
        else:
            print("NO")
    else:
        p=math.ceil(l/2)
        if sorted(S[:p-1])==sorted(S[p:]):
            print("YES")
        else:
            print("NO")