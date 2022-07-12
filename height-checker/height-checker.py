class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Solution: O(n) time, O(n) additinal space.
        expected = sorted(heights)
        return sum((1 for height, expect in zip(heights, expected) if height != expect))