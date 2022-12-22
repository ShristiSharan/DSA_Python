class Solution(object):
    def runningSum(self, nums):
        new=[]
        sum=0
        for i in range(len(nums)):
             sum=sum + nums[i]
             new.append(sum)
        return(new)


    # eg: Input- nums=[1,2,3,4]
    #    Output- [1,3,6,10]

