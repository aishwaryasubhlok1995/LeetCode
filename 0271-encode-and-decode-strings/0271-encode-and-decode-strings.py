class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enStr = ''
        for i in range(len(strs)):
            strs[i] = strs[i].replace('#', '##')
            enStr += strs[i] + '#?'
        print(enStr)
        return enStr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        j = 0
        curr = ''
        while j<len(s):
            if s[j] != '#':
                curr += s[j]
                j += 1
            else:
                if s[j + 1] == '#':
                    curr += '#'
                else: 
                    ans.append(curr)
                    curr = ''
                j += 2

        return ans