class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = s.encode()  
        cap = len(set(data)) if len(data) > 512 else 256

        last = [0] * 256

        best = left = right = 0
        for b in data:
            right += 1
            prev = last[b]
            if prev > left:
                left = prev
            elif right - left > best:
                best = right - left
                if best == cap:
                    break  
            last[b] = right

        return best