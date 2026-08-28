class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s="".join(it for it in s if it.isalnum())
        return s==s[::-1]