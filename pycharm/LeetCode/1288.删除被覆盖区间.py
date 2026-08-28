# class Solution(object):
#     def removeCoveredIntervals(self, intervals):
#         sorted_matrix=sorted(intervals,key=lambda x:(x[0],-x[1]))
#         covered_num=0
#         for it1 in range(1,len(sorted_matrix)):
#             for it2 in range(0,it1):
#                 if sorted_matrix[it2][-1]>=sorted_matrix[it1][-1]:
#                     covered_num+=1
#                     break
#         return len(sorted_matrix)-covered_num
#
# class Solution(object):
#     def removeCoveredIntervals(self, intervals):
#         covered_num=0
#         sorted_intervals = sorted(intervals, key=lambda x: (x[0],-x[1]))
#         back_list=list(zip(*sorted_intervals))[1]
#         for it in range(1,len(sorted_intervals)):
#             front_list=back_list[:it]
#             if back_list[it]<=max(front_list):
#                 covered_num+=1
#         return len(sorted_intervals)-covered_num

class Solution:
    def removeCoveredIntervals(self, intervals):
        covered_num=0
        max_end=0
        sorted_intervals = sorted(intervals, key=lambda x: (x[0],-x[1]))
        for it in sorted_intervals:
            if it[1]>max_end:
                max_end = it[1]
                continue
            covered_num+=1
        return len(sorted_intervals)-covered_num