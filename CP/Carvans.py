# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    check=0 
    S=list(map(int,input().split()))
    prevspeed=S[0]
    for i in S:
        # for j in range(i+1,N):
        if prevspeed>=i:
            check+=1
            prevspeed=i
    print(check)