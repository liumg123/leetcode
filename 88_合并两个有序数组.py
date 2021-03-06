"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and nums2:
            r=0
            while r<n:
                nums1[r]=nums2[r]
                r+=1
        if m>0 and nums2 and nums1:
            l,r=0,0
            while l<m+n and r<n:
                if nums1[l]<nums2[r]:
                    l+=1
                else:
                    nums1.insert(l,nums2[r])
                    r+=1
            try:
                nums1[m+r:]=nums2[r:]
            except:
                pass
            