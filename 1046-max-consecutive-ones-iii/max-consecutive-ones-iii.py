class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeroCount = 0 

        for num in nums:
            if num == 0:
                zeroCount += 1
            

            if zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
        return len(nums)- left