class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        freq={}
        if s == "" and t == "":
            return True
        elif s == None or t == None:
            return False
    
        else:
            if (len(s)!=len(t)):
                 return False
            
            for i in range(0, len(s)):
                d = s[i]
                f = t[i]

                if d in freq:
                    if freq[d] != f:
                        return False
                else:
                    if f in freq.values():
                        return False
                    freq[d] = f
            return True

# sol = Solution()
# s = "abc"
# t = "abhcd"
# print(sol.isIsomorphic(s, t))

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "abhcd"
    print(sol.isIsomorphic(s, t))


        


#****************************************************************************************  
  

# def Iso(self,s,t):
#     d=[]
#     f=[]

#     if (len(s)==len(t)):
#              for c in s:
#                  count=s.count(c)
#                  if count>1:
#                    d.append(count)
#              for c in t:
#                count=t.count(c)
#                if count>1:
#                    f.append(count)
#              if d==f:
#                 return True
#              else:
#                  return False
#     else:
#         return False


