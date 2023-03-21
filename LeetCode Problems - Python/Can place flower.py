class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        l=len(flowerbed)
        if n==0:
          return True
        for i in range(l):
            if (flowerbed[i]==0) and (i==0 or flowerbed[i-1]==0) and (i==l-1 or flowerbed[i+1]==0):
                count+=1
                if(count>=n):
                    return True
                flowerbed[i]=1
        return False
            
                
   