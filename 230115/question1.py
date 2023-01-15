class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([self.cal(num) for num in nums])
    def cal(self, num):
        result = 0
        now = 0
        while num != 0:
            result += (num % 10) * (10**now - 1)
            now += 1
            num //= 10
        return result


A = Solution()
A.differenceOfSum([725, 23])