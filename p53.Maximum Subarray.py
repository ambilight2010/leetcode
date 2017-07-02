class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.dp(nums)
        return self.divide(nums)

    def dp(self, nums):
        if not nums: return 0
        cur_sub = 0
        max_sub = nums[0]
        for n in nums:
            cur_sub = max(cur_sub + n, n)
            max_sub = max(cur_sub, max_sub)
        return max_sub

    def divide(self, nums):
        def helper(nums, left, right):
            if left == right:
                return nums[left]
            if left + 1 == right:
                return max(nums[left] + nums[right], nums[left], nums[right])
            mid = (left + right) // 2
            left_max = helper(nums, left, mid - 1)
            right_max = helper(nums, mid + 1, right)
            mid_max = nums[mid]

            tmp = mid_max
            for i in range(mid - 1, left - 1, -1):
                tmp += nums[i]
                mid_max = max(mid_max, tmp)

            tmp = mid_max
            for i in range(mid + 1, right + 1):
                tmp += nums[i]
                mid_max = max(mid_max, tmp)

            return max(left_max, right_max, mid_max)

        return helper(nums, 0, len(nums) - 1)

