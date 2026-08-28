from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        def compare(num1,num2):
            if num1+num2>num2+num1:
                return -1
            elif num1+num2<num2+num1:
                return 1
            else:
                return 0
        nums_str=list(map(str,nums))
        nums_str.sort(key=cmp_to_key(compare))
        return_str="".join(nums_str)
        return return_str if int(return_str)!=0 else "0"