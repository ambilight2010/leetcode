class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        cur_max, cur_min = 1, 1
        for n in nums:
            cur_max, cur_min = max(cur_min * n, cur_max * n, n), min(cur_min * n, cur_max * n, n)
            result = max(result, cur_max)
        return result
