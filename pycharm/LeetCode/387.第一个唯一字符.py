class Solution(object):
    def firstUniqChar(self, s):
        for it in s:
            if s.find(it)==s.rfind(it):
                return s.index(it)
        return -1