class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool 
        """
        if word.isupper() or word.islower():
            return True
        elif word.capitalize() == word:
            return True
        return False

##Input: word = "USA"      ,,, word="flag"       ,,, word ="Leetcode"  ,,,  word: "HeLlo"
##Output: true             ,,, : false           ,,,  : true           ,,,   :false

        