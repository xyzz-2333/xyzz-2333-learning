#分析：
'''如果nums1均为奇数或者偶数：nums2[i] = nums1[i]即可
如果nums1为混合：
分析1奇1偶的情况：直接奇-偶（如果奇>偶）或偶-奇即可
当nums1增加新数字时：情况不变
∴：始终有解
写什么代码，直接return即可'''
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True