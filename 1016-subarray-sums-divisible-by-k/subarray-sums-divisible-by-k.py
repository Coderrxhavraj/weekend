class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * k
        cnt[0] = 1
        rem = 0
        res = 0
        for num in nums:
            rem = (rem + num) % k
            res += cnt[rem]
            cnt[rem] += 1
        return res