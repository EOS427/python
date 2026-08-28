# class KthLargest(object):
#
#     def __init__(self, k, nums):
#         self.target_rank=k
#         self.seek_k_list=nums
#         if self.target_rank>len(self.seek_k_list):
#             self.rank_k_num:int=sorted(nums,reverse=True)[-1]
#         else:
#             self.rank_k_num:int=sorted(nums,reverse=True)[k-1]
#
#     def add(self, val):
#         self.seek_k_list.sort()
#         if self.target_rank==len(self.seek_k_list):
#             if self.rank_k_num>val:
#                 self.rank_k_num=val
#         elif self.target_rank==1:
#             if val>self.seek_k_list[0]:
#                 self.rank_k_num=val
#         else:
#             front_num=self.seek_k_list[self.target_rank-2]
#             back_num=self.seek_k_list[self.target_rank]

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k
        self.heap=[]
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


