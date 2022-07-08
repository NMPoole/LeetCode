class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Solution using bitwise operations.
        #   Num steps = num divs + num subs
        #             = num bit shifts + num subs : num bit shifts to move most significant one to least sig. place.
        #             = num bits - 1 + num ones : num subs is num 1s seen when shifting requiring sub to get even num again.
        
        bit_str = bin(num)[2:] # [2:] will remove the '0b' that is prepended to each bitstring by bin().
        return len(bit_str) - 1 + bit_str.count('1')
        