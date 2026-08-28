class Solution(object):
    def twoSum(self, numbers, target):
        if len(numbers)<2:return []
        left=0
        right=len(numbers)-1
        numbers.sort()
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum<target:
                while numbers[left]==numbers[left+1]:left+=1
                left+=1
            elif sum>target:
                while numbers[right]==numbers[right-1]:right-=1
                right-=1
        return []


