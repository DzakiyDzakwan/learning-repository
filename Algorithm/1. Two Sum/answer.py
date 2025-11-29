# My Solution
class Solution(object):
    def twoSum(self, nums, target):
        previous_num = 0
        result = False
        results = []

        for i in range(len(nums)):
            for j in range(len(nums) - (i+1)):
                if nums[i] + nums[j+i+1] == target : 
                    results =[i, j+i+1]
                    result = True
                    break
            if result:
                break
                
        return results

# Top Solution
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        dict1 = {}

        for i in range(n):
            rem = target - nums[i]
            if rem in dict1:
                return [dict1[rem], i]
            dict1[nums[i]] = i