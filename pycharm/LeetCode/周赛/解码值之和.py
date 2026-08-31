class Solution(object):
    def sumDecoded(self, nums):
        sum=0
        order=10**9
        modulo=order+7
        for num in nums:
            width=num%10
            d=num//10
            length=10**(len(str(d))-width)
            x=d//length
            y=d-x*length
            decode=pow(x,y,modulo)
            sum+=decode
        return int(sum%modulo)

def main():
    solution=Solution()
    # nums=input()
    print(solution.sumDecoded([55162,86552]))

if __name__=="__main__":
    main()