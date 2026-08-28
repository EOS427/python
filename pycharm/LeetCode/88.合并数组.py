class Solution(object):
    def merge(self, nums1, m, nums2, n):
        list1=nums1[:m]
        list2=nums2[:n]
        list1.extend(list2)
        nums1[:]=sorted(list1)
        return nums1
