class Solution(object):
    def twoSum(self, nums, target):
        for it1 in range(len(nums)):
            for it2 in range(it1+1,len(nums)):
                if nums[it1]+nums[it2]==target:
                    return [it1,it2]
        return []