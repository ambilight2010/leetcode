class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums) - 1
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[n]:
                if nums[mid] < target <= nums[n]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
