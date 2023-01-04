### Problem 2244.Minimum Rounds to Complete All Tasks            
def minimumRounds(self,tasks):
    import math
    diction={}
    count=0
    merge=0
    for i in range(0,len(tasks)):
        for j in range(0,len(tasks)):
            if tasks[i]==task[j]:
                count+=1
                diction[tasks[i]]=count
            count=0
            
    for value in diction:
            (value//2)=store
            new=math.floor(store)
            x=value-new
            if (x % 2==0):
                x/2=check
                merge+=check
            elif(x % 3==0):
                x/3=check
                merge+=check
            
    return merge
            