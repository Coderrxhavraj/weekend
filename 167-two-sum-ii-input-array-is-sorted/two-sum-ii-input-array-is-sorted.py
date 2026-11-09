class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l = bisect_left(numbers, target - numbers[r])
            else:
                r = bisect_right(numbers, target - numbers[l]) - 1