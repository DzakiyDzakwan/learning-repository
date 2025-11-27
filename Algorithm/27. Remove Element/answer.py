class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        while i < len(nums) :
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return i
    
# Alternate Solution
# class Solution(object):
#     def removeElement(self, nums, val):
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 count += 1
#             else:
#                 nums[i-count] = nums[i]
#         return len(nums) - count