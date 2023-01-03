class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        col=len(strs[0])
        row=len(strs)
        count=0
        for i in range(col):                  ### i fixing over char index of each word(seperated by ,)
            for j in range(1,row):            ### j working over the index of main list strs
                if strs[j-1][i]> strs[j][i]:  ##basically checking each
                    count+=1
                    break
        return count

  ### input: strs=["cba","daf","ghi"]    
  ## output: 1    (as the column wise sequence  wansn't sorted so 1 col has to be deleted and thus returned.)