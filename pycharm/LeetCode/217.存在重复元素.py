class Solution(object):
    def containsDuplicate(self, nums):
        numset=set(nums)
        if len(numset)==len(nums):return False
        return True