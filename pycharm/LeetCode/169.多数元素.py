class Solution(object):
    def majorityElement(self, nums):
        minTime=len(nums)//2
        count={}
        for it in nums:
            if it not in count:
                count[it]=1
            else:count[it]+=1
        for it in count:
            if count[it]>minTime:
                return it
        return