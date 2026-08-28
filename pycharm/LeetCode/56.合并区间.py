class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:return []
        intervals.sort(key=lambda x:(x[0],x[1]))
        merged_list=[]
        current_list=intervals[0]
        for index in range(1,len(intervals)):
            if intervals[index][0]<=current_list[1]:
                if current_list[1]>=intervals[index][1]:
                    continue
                else:current_list=[current_list[0],intervals[index][1]]
            else:
                merged_list.append(current_list)
                current_list=intervals[index]
        if current_list not in merged_list:
            merged_list.append(current_list)
        return merged_list

def main(s):
    solution = Solution()
    solution.merge(s)

if __name__=="__main__":
    main([[1,3],[2,6],[8,10],[15,18]])
