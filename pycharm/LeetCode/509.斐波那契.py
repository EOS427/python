class Solution(object):
    def fib(self, n):
        counted_map={}
        def checkAndCount(x):
            if x in counted_map:
                return counted_map[x]
            if x<=1:
                counted_map[x]=x
                return x
            counted_map[x]=checkAndCount(x-1)+checkAndCount(x-2)
            return counted_map[x]
        return checkAndCount(n)