from collections import Counter, defaultdict
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = defaultdict(int)
        result = 0
        now_k = 0
        end_idx = -1
        for i in range(0, len(nums)):
            while True:
                if now_k < k:
                    end_idx += 1
                    if end_idx == len(nums):
                        return result
                    else:
                        now_k += A[nums[end_idx]]
                        A[nums[end_idx]] += 1
                else:
                    result += len(nums) - end_idx
                    print(len(nums) - end_idx, end=" ")
                    break
            A[nums[i]] -= 1
            now_k -= A[nums[i]]

A = Solution()
nums = [1,7,4,2,9,7,3,3,7,2,3,5]
k = 3
A.countGood(nums, k)