class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ''
        for i in strs:
            if i == '':
                ans += 'None' + '[*/]' 
            else:
                ans += i + '[*/]'
        return ans
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        for i in (s.split('[*/]')):
            if i == 'None':
                ans.append("")
            elif i != '':
                ans.append(i)
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))