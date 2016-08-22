"""
Space - O(k)
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        res = []
        
        for i in xrange(numRows):
            row = []
            for j in xrange(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            res.append(row)
            prev = row            
        
        return res
                    
"""
Space - O(k)
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        1
        11
        121
        1331
        14641
        """
        if rowIndex == 0:
            return [1]
        
        row = [0 for i in xrange(rowIndex+1)]
        
        for i in xrange(rowIndex+1):
            for j in xrange(i, -1, -1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] += row[j-1]
        
        return row
            
        
        
