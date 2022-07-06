class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(n) time complexity and O(n) space complexity.
        counts = Counter(nums1) # Frequency counts of numbers in nums1.
        output = []
        
        for num in nums2:
            if counts[num] > 0:
                output.append(num)
                counts[num] -= 1 # Only add a number as many times at it appears in both lists.
                
        return output