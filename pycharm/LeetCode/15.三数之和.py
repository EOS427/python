class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        count = []
        edge=len(nums)-1
        for i in range(edge):
            if i>1 and nums[i]==nums[i-1]:continue
            if nums[i]>0:break
            left=i+1
            right=edge
            while left<right:
                result=nums[right]+nums[left]+nums[i]
                if result==0:
                    if [nums[i],nums[left],nums[right]] not in count:
                        count.append([nums[i],nums[left],nums[right]])
                    else:break
                    while left<right and nums[left]==nums[left+1]:left+=1
                    while left<right and nums[right]==nums[right-1]:right-=1
                    left+=1
                    right-=1
                elif result>0:
                    right-=1
                else:left+=1
        return count