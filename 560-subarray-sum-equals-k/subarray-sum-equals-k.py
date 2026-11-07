class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        - input: given int array nums and int k  
        - output: return total number of subarrays whose sum equals k (int)

        - logic:
            - a subarray is contigious non-empty sequence of elements within an array
                - my first thought is i want to calculate the sum of contigious elements so a sliding window
                - a sliding window on the original array might be expensive since we would have to check all combinations of subarrays which would be O(n^3)
                - if we sort the array first we can have a variable sliding window where we add eleents using the right pointer and subtract elements using the left
                - since its sorted we can add an element if our sum is too small and subtract an element if our sum is too big
                - once we get a match we can increment both pointers and then go from there 
            - realized we can't do that since if we sort we lose the contiguous part 
                - what if we have two pointers and if we are too big we move the pointer that points to the bigger element
                - and if we are too small we move the smaller of the pointers
        """

        n = len(nums)
        prefix_counts = {0:1}
        matches = 0
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            matches += prefix_counts.get(cur_sum-k, 0)
            prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1

        return matches

