class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # Solution: O(m n) time, O(n) additional space.
        
        d = collections.defaultdict(list) # Dictionary contains elements along the diagonals in 'North-East' direction.
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])
                
        ans = []
        
        for entry in d.items():
            if entry[0] % 2 == 0: # This flips the direction elements are added by (i.e., snaking through matrix).
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
                
        return ans