class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        prefix_counts = {0:1}
        matches = 0
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            matches += prefix_counts.get(cur_sum-k, 0)
            prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1

        return matches

