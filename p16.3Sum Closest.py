class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t == target:
                    return t
                elif t < target:
                    j += 1
                else:
                    k -= 1
                if abs(t - target) < abs(result - target):
                    result = t
        return result
