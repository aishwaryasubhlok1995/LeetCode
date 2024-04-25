class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for i in range(len(emails)):
            strinEmails = emails[i].split('@')
            stringFirstHalf  = strinEmails[0].split('+')[0].replace('.', '')
            element =  stringFirstHalf + '@' + strinEmails[1]
            ans.add(element)
        return len(ans)
        