N = int(input())
for i in range (0,N):
    W,L,M,X,Y = input().split()
    A = int(M)-int(X)
    B = int(M)-int(Y)
    if(A>= int(W)):
        if(B>=int(W)):
            print("JUMP")
        else:
            print("FALL")
    else:
        print("FALL")
    
#Can the spider run :
# decode 
# spider wieghs W, web of circle of layer L 
# W<=strength of current pos 
# center strength =M while webing layers 
# each layer strength dec by 1
# center=m
# L=1 then=m-1
# L=2 then=m-2
# ...strength of each layer is M-L


# Xth layer to Yth layer ---
# W,L,M,X,Y 