#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Brute force method
        for i in range(len(nums)):
            for n in range(i+1, len(nums)):
                if nums[n]+nums[i]==target:
                    return[n, i]
        return
        """

        hash = {}
        for i, n in enumerate(nums):
            temp = target-n
            if temp in hash:
                return [hash[temp], i]
            hash[n] = i
        return

        