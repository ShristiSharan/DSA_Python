def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l=len(str2)
        store=str1[0:l]
        if store==str2:
            output=str1[l:]
        else:
            output = ""

        return(output)

