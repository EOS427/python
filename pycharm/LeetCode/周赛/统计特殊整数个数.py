class Solution(object):
    def countSpecialIntegers(self, nums):
        if not nums:
            return None
        if len(nums)==1:
            return 1

        num_map={}
        previous_num=nums[0]
        num_map[previous_num]=1
        for index in range(1,len(nums)):
            current_num=nums[index]
            if current_num!=previous_num:
                if current_num not in num_map:
                    num_map[current_num]=1
                else:
                    num_map[current_num]+=1
            previous_num=current_num

        sum=0
        for value in num_map.values():
            if value==1:
                sum+=value
        return sum

def main():
    # num_str=input()
    # nums=list(num_str)
    solution=Solution()
    print(solution.countSpecialIntegers([34,34]))

if __name__=="__main__":
    main()