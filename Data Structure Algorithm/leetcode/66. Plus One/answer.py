class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        remain = 1
        i = len(digits) - 1

        while i > -1:
            if digits[i] + remain > 9:
                digits[i] = 0
            else :
                digits[i] = digits[i] + remain
                remain = 0
            
            i -= 1
        
        if remain:
            digits.insert(0, remain)
        
        return digits