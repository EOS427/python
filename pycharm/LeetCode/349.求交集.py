class Solution(object):
    def intersection(self, nums1, nums2):
# intersection={it for it in set(nums1) if it in set(nums2)}
# return list(intersection)
#        return list(set(nums1)&set(nums2))
         return list(set(nums1).intersection(set(nums2)))