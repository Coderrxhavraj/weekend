class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = best = sum(s.count(v, 0, k) for v in "aeiou")

        if best == k or k == len(s):
            return best

        
        table = bytes(1 if c in b"aeiou" else 0 for c in range(256))
        flags = s.encode().translate(table)

        for outgoing, incoming in zip(flags, flags[k:]):
            if incoming:
                if not outgoing:
                    # A vowel replaces a consonant: count increases.
                    count += 1
                    if count > best:
                        best = count
                        if best == k:
                            return k
            elif outgoing:
                count -= 1

        return best