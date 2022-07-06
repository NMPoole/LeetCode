class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse(0, n - 1, nums) # Reverse the whole list.
        self.reverse(0, k - 1, nums) # Reverse just the first k items.
        self.reverse(k, n - 1, nums) # Reverse all items after first k.
            
    def reverse(self, l, r, arr):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1
            
        return arr
        