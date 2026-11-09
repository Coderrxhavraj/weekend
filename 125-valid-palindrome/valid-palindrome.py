import string
table: dict[int, None] = {ord(i):None for i in string.punctuation + string.whitespace}
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.translate(table).lower()
        return res == res[::-1]