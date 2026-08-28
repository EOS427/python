class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        return self.seakLongestSubString(s,0, {})

    def seakLongestSubString(self,s,startIt,counter):
        if len(s)==1 or startIt==len(s)-1:return 1
        for currentIt in range(startIt,len(s)):
            if s[currentIt] not in counter:
                counter[s[currentIt]]=currentIt
            else:
                break
        else:
            return len(s)-startIt
        repeatedIt=counter[s[currentIt]]
        counter.clear()
        restLongest=self.seakLongestSubString(s,currentIt,counter)
        # counter.clear()
        # restLongest=self.seakLongestSubString(s,repeatedIt+1,counter)
        currentLongest=currentIt-startIt
        return max(restLongest,currentLongest)

def main():
    string=input()
    solution = Solution()
    print(solution.lengthOfLongestSubstring(string))

# if __name__ == '__main__':
main()