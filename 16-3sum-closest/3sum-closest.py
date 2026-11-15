class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
    
        output = nums[0] + nums[1] + nums[2]
        if output > target:
            return output

        max_sum = nums[-1] + nums[-2] + nums[-3]
        if max_sum < target:
            return max_sum

        difference = abs(target - output)
        
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            s = nums[i] + nums[i + 1] + nums[i + 2]
            if s >= target:
                if s - target < difference:
                    output = s
                break

            s = nums[i] + nums[-1] + nums[-2]
            if s < target:
                if target - s < difference:
                    output, difference = s, target - s
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                dif = abs(target - total)
                if total == target:
                    return target
                if dif < difference:
                    difference = dif
                    output = total

                if total < target:
                    l += 1
                else:
                    r -= 1

        return output