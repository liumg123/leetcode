"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a=nums[i]+nums[j]
                b=nums[j]+nums[i]
                if a<=b:
                    nums[i],nums[j]=nums[j],nums[i]
        if list(set(nums))[0]=="0" and len(list(set(nums)))==1:
                return "0"
        return ''.join(nums)