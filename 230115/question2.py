
from numpy import array
class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        A = array([[0 for _ in range(n) ]for _ in range(n)])
        for row1, col1, row2, col2 in queries:
            A[row1:row2+1, col1:col2+1] += 1
        return A



A = Solution()
n = 3
queries = [[1,1,2,2],[0,0,1,1]]
A.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]])
