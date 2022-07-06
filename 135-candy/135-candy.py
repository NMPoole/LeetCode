class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1 for _ in range(n)] # Output array of candies, O(n) space.
        
        for i in range(1, n): # Greater rating gives more candy on left neighbours.
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1): # Greater rating gives more candy on right neighbours.
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        
        return sum(candies) # Minimum is thre sum of all assigned candies in the candies array.