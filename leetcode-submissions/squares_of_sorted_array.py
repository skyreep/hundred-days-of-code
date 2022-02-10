class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = []
        for num in nums:
            new_nums.append(num * num)
        new_nums.sort()
        return new_nums