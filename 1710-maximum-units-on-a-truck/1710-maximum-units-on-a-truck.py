class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key= lambda x: -x[1])
        
        capacity = 0
        
        for numBoxes, unitsPerBox in boxTypes:
            
            if truckSize >= numBoxes: # If can fit all of the boxes, then take all.
                truckSize -= numBoxes
                capacity += numBoxes * unitsPerBox
            
            else: # If can't fit all boxes, then take remaining amount allowed.
                capacity += truckSize * unitsPerBox
                break
                
        return capacity
        