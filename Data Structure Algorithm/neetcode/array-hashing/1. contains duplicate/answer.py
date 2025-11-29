class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed_number = []

        for num in nums:
            if num in existed_number:
                return True
            else:
                existed_number.append(num)
            
        return False