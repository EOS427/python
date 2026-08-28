class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        myjewellist=dict.fromkeys(tuple(jewels),0)
        for it in stones:
            if it in myjewellist:
                myjewellist[it]+=1
        return sum(myjewellist.values())