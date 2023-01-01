def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s) 

        # this approach could also achieve to submission but few edges cases needs to be resolved...11/18 !!
        # if len(s)>len(t):


        # count=0
        # for char in set(s):
        #     if char in set(t):
        #         count+=1
        #     else:
        #         break
        
        # if count==len(set(s)):
        #     return True
        # else:
        #     return False