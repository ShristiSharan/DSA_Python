class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for _ in range(numRows)]
        row = 0
        step = 1
        for c in s:
            zigzag[row] += c
            if row == numRows-1:
                step = -1
            elif row == 0:
                step = 1
            row += step
        return ''.join(zigzag)          
    

### Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I