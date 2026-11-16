class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        limit = 2 * min(ones, n - ones)
        if limit == n or limit == 0:
            return limit
        first = [None] * (2 * n + 1)
        first[0] = -1
        balance = answer = 0
        for i, value in enumerate(nums):
            balance += 1 if value else -1
            start = first[balance]
            if start is None:
                first[balance] = i
            else:
                length = i - start
                if length > answer:
                    answer = length
                    if answer == limit:
                        return answer
        return answer
