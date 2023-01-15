## fail to be accepted

class Solution(object):
    def maxOutput(self, n, edges, price):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :rtype: int
        """

        def max_route(node_idx, drop):
            result = 0
            for leaf_idx in A[node_idx]:
                if leaf_idx != drop:
                    result = max(result, max_route(leaf_idx, node_idx))
            return result + price[node_idx]

        A = [[] for _ in range(n)]
        is_leaf = [1 for _ in range(n)]
        for begin, end in edges:
            A[begin].append(end)
            A[end].append(begin)
            is_leaf[begin] += 1
            is_leaf[end] += 1
        result = 0
        for node_idx in range(n):
            if is_leaf[node_idx] == 2:
                result = max(result, max_route(A[node_idx][0], node_idx))
        return result



n = 6
edges = [[0,1],[1,2],[1,3],[3,4],[3,5]]
price = [9,8,7,6,10,5]
A = Solution()
A.maxOutput(n, edges, price)