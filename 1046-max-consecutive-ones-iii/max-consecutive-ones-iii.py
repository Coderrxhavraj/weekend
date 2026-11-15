class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, i = 0,0 
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
        return len(nums)-left
        