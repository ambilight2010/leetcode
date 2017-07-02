class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i = 0
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > target:
                i -= 1
                break
        if matrix[i][0] > target:
            return False
        for num in matrix[i]:
            if num == target:
                return True
        return False
