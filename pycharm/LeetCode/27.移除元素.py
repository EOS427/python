class Solution(object):
    def removeElement(self, nums, val):
        if nums==[]:return 0
        self.deleteRepeatNum(nums,val,0)

    def deleteRepeatNum(self, nums, val,ptr):
        if ptr==len(nums):
            return
        if nums[ptr]==val:
            nums.pop(ptr)
        else:ptr+=1
        self.deleteRepeatNum(nums,val,ptr)
        return len(nums)