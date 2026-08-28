class Solution(object):
    def removeDuplicates(self, nums):
        if nums==[] or len(nums)==1:return len(nums)
        self.deleteRepeatNode(nums,0,1)

    def deleteRepeatNode(self,nums,leftPtr,rightPtr):
        if nums[leftPtr]==nums[rightPtr]:
            nums.pop(rightPtr)
            if leftPtr==len(nums)-1:
                return
        else:
            if rightPtr == len(nums) - 1:
                return
            leftPtr+=1
            rightPtr+=1
        self.deleteRepeatNode(nums,leftPtr,rightPtr)