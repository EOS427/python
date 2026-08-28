from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        str_dict=defaultdict(list)
        for it in strs:
            key =''.join(sorted(it))
            str_dict[key].append(it)
        return list(str_dict.values())
