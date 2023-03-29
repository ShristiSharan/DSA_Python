# cook your dish here
T=int(input())
for i in range(T):
    k,d0,d1=list(map(int,input().split()))
    # 2<=i<k di=(d0+.....dk-1)*mod (10)
    D=d0+d1
    for j in range(2,k):
        D+=D%10
        if (k - j - 1) % 12 == 0:
            break
    if D % 3 ==0:
        print("YES")
    else:
        print("NO")