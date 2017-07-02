class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = [-2**32, -2**32, -2**32]
        min_nums = [2**32, 2**32]
        for n in nums:
            if n > max_nums[0]:
                max_nums[0:] = n, max_nums[0], max_nums[1]
            elif n > max_nums[1]:
                max_nums[1:] = n, max_nums[1]
            elif n > max_nums[2]:
                max_nums[2] = n

            if n < min_nums[0]:
                min_nums[0:] = n, min_nums[0]
            elif n < min_nums[1]:
                min_nums[1] = n
        return max(max_nums[0] * max_nums[1] * max_nums[2], max_nums[0] * min_nums[0] * min_nums[1])
