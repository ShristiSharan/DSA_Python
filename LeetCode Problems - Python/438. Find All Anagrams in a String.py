class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Los=len(s)                  #Lop=length of  p
        Lop=len(p)                  #Los=length of s
        S= 0
        P=0
        res=[]
        if Lop > Los:                         
            return []
        for i in range(Lop): S, P = S + hash(s[i]), P + hash(p[i])
        if S == P:
            res.append(0)
        for i in range(Lop, Los):
            S += hash(s[i]) - hash(s[i-Lop])
            if S == P:
                res.append(i-Lop+1)
        return res
    
#Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

#basically frequency count using hashing.


#Anagram: sorted(s1)==sorted(s2)-------is anagram! else not!!!