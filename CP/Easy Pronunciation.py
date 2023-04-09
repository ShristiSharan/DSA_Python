T=int(input())
for i in range(T):
    N=int(input())
    s=input()
    check=0
    count=0
    for i in s:
        if i not in ['a','e','i','o','u']:
            count+=1
        else:
            count=0    #to nullify and break when vowel meet as it stores count in temp variable check
    
        if count>check:
            check=count
    if check>=4:
        print("NO")
    else:
        print("YES")