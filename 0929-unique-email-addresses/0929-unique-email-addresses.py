class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for i in range(len(emails)):
            strinEmails = emails[i].split('@')
            stringFirstHalf  = strinEmails[0].split('+')[0].replace('.', '')
            ans.add(stringFirstHalf + '@' + strinEmails[1])
        return len(ans)
        