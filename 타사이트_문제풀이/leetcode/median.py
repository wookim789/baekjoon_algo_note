class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1 + nums2
        l = len(nums1)
        nums1.sort()
        result = 0
        if l % 2 == 0:
            a = l // 2 - 1
            result = (nums1[a] + nums1[a + 1]) / 2.0
        else:
            result = nums1[l // 2]
        return result
        