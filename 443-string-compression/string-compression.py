class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 0:
            return 0
        
        left = 0
        right = 0
        n = len(chars)
        
        while right < n:
            current_char = chars[right]
            start = right
            while right < n and current_char == chars[right]:
                right = right + 1

            count = right - start
            chars[left] = current_char
            left = left + 1
            if count > 1:
                for ch in str(count):
                    chars[left] = ch
                    left = left + 1
        return left