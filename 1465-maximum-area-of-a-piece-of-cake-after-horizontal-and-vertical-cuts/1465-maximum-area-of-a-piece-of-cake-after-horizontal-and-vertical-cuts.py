class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        # Sort both arrays.
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Compute maximum difference between consecutive elements.
        maxDiffHor = self.maxElementDiff(horizontalCuts)
        maxDiffVer = self.maxElementDiff(verticalCuts)
        
        # Max area is product of two numbers.
        return (maxDiffHor * maxDiffVer) % (10**9 + 7)
    
    
    def maxElementDiff(self, list1):
        if len(list1) == 1:
            return list1[0]
        else:
            return max((list1[i+1] - list1[i] for i in range(len(list1) - 1)))
        