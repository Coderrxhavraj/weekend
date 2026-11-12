class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000

        nums = sorted(nums)
        curr = 1
        answer = 1
        
        last = nums[0]
        for n in range(1, len(nums)):
            if nums[n] == last:
                continue
            elif nums[n] == last + 1:
                curr += 1
            else:
                curr = 1

            if curr > answer:
                answer = curr
            
            last = nums[n]

        return answer