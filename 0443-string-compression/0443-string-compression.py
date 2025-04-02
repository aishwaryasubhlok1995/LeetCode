class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 1
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i-1]:
                if count > 1:
                    for c in str(count):
                        chars[j] = c
                        j += 1
                    chars[j] = chars[i]
                else:
                    chars[j] = chars[i]
                j += 1
                count = 1
            else:
                count += 1
        if j < len(chars):
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
                return j
        return j


        