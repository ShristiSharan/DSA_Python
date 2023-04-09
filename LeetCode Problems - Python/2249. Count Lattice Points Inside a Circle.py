class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        res=set()
        for x,y,r in circles:
            for i in range(x - r,x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (x - i) ** 2 + (y - j) ** 2 <= r * r:
                        res.add((i,j))
        return(len(res))
        
# meaning of single (*)-- Unpacking a function using positional argument.
# This method is very useful while printing your data in a raw format (without any comma and brackets )
# Passing a Function Using with an arbitrary number of positional arguments
# it is mostly used to pass a non-key argument and variable-length argument list.


#meaning of double(**)--This special symbol is used to pass a keyword arguments and variable-length argument lists.