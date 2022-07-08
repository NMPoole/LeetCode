class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((len(str(i))) % 2 == 0 for i in nums)