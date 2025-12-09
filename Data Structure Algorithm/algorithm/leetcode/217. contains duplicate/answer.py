class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed_number = []

        for num in nums:
            if num in existed_number:
                return True
            else:
                existed_number.append(num)
            
        return False
    
# Alternate Solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()

        for num in nums:
            if num in number_set:
                return True
            else:
                number_set.add(num)
        
        return False