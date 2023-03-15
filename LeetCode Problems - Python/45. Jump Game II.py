class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#basically shift to index 1 from index 0 ......then whatever the num[i]==value take that leap jump to that upto the length,
# making sure that it completes the whole length of the nums array.

        jumps=0
        curr=0
        curr_far=0
        n=len(nums)
        for i in range(n-1):
            curr_far=max(curr_far,i+nums[i])
            if(i==curr):
                jumps+=1
                curr=curr_far
        return jumps
   
        