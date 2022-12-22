def Concat(self,nums):
    rep_num=nums
    que=[]
    for i in nums:
         que.append(i)
    for i in rep_num:
         que.append(i)
#output= [nums,rep_num]
    print(que)

    #eg: input: nums=[1,2,3]
    #    output: [1, 2, 3, 1, 2, 3]