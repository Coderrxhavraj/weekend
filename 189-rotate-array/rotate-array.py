class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = nums[len(nums)-k:]
        del nums[len(nums)-k:]
        nums[0:0] = n
        
        