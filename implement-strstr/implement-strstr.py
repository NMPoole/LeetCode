class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Solution: "O((n-m)*m) time - n is the size of haystack, and m is the size of needle."
        # Problem is trivial in Python, but doesn't adhere to the point of the question.
        return haystack.find(needle)