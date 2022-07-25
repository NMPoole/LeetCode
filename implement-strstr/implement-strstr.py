class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Solution: "O((n-m)*m) time - n is the size of haystack, and m is the size of needle."
        return haystack.find(needle)