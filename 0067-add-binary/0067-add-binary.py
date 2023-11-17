class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        final = ''
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while i>=0 or j>=0:  
            if i<0:
                sum = int(b[j]) + carry
            elif j<0:
                sum = int(a[i]) + carry
            else:
                sum = int(a[i]) + int(b[j]) + carry
            if sum > 1:
                carry = 1
                if sum == 2:
                    final = '0' + final 
                if sum > 2:
                    final = '1' + final 
            else:
                final = str(sum) + final 
                
                carry = 0
            i -= 1
            j -= 1
            
        if carry == 1:
            final = '1' + final
        return final
            
        
        