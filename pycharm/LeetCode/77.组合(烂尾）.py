import copy
class Solution(object):
    def combine(self, n, k):
        if n<k:return []
        return self.seakCombination(n,k,1)

    def seakCombination(self,n,k,start,track,current,list):
       if start==n-k+2:return list
       for it in range(current,n-k+2):
           track.append(it)
           self.seakCombination(n,k,start,track,it,list)

       if len(track)==k:
           list.append([track])
           track=[]
           if start != n-k+2:
               self.seakCombination(n,k,start+1,track,start+1,list)

    # def seakCombination(self,n,k,phase):
    #     if phase==k+1:return None
    #     currentList=[]
    #     for it in range(phase,n-k+phase-1):
    #         semiList= [it]
    #         returnValue=self.seakCombination(n,k,phase+1)
    #         if returnValue:
    #             semiList.extend(returnValue)
    #         if phase==1:
    #             currentList.append(semiList)
    #         else:currentList=copy.deepcopy(semiList)
    #     return currentList