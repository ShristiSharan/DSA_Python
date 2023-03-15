
        # l=len(str2)
        # store=str1[0:l]
        # if store==str2:
        #     output=str1[l:]
        # else:
        #     output = ""

        # return(output)

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # l=len(str2)
        # store=str1[0:l]
        # if store==str2:
        #     output=str1[l:]
        #     return(output)
        # else:
        #     return("")
        if len(str1)<=len(str2):
             temp = str1
        else:
            temp = str2
        m = len(temp)
        x = 1
        res=[""]
        while x<=m:
            if m%x==0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
                res.append(temp[:x])
            x+=1
        return res[-1]



        

 

