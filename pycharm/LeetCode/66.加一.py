class Solution(object):
    def plusOne(self, digits):
        return self.adder(digits,1,0,1)

    def adder(self,digits,currentDigit,carry,added):
        if len(digits)<currentDigit:
            digits.insert(0,carry)
            realNum=carry+added
        else:
            realNum = digits[len(digits)-currentDigit] + carry + added
        leftNum = realNum % 10
        digits[len(digits)-currentDigit]=leftNum
        carry=(realNum-leftNum)//10
        if carry>0:self.adder(digits,currentDigit+1,carry,0)
        return digits
