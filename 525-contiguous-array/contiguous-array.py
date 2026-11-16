
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_length = 0

        hashmap = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in hashmap:
                max_length = max(
                    max_length, i - hashmap[prefix_sum]
                )
            else:
                hashmap[prefix_sum] = i

        return max_length
