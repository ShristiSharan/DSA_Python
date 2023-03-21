class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we need to input the list and check for zeors 
        #first count the appearance in total and let it stored
        count=0  #for consecutive count of zeros
        store=0
        l=len(nums)
        for i in range(l):
            if (nums[i]==0):
                count+=1
                store+=count
            else:
                count=0
        return(store)
                            
        


        
        