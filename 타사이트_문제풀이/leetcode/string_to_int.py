class Solution(object):
    def myAtoi(self, s):
        if not s :
            return 0
        
        if not (48 <= ord(s[0]) <= 57) and s[0] != '-' and s[0] != '+' and s[0] != ' ':
            return 0
        
        s = s.strip()
        
        result = ""
        for c in s:
            if not result and (c == '-' or c == '+'):
                result += c
            elif 48 <= ord(c) <= 57:
                result += c
            else:
                break
                
        if not result:
            return 0
        
        elif result == '-' or result == '+':
            return 0
        
        elif result.count('-') + result.count('+') > 1:
            return 0
        
        result = int(result)
        
        if result >= 2 ** 31:
            result = 2 ** 31 - 1
            
        elif result <= -(2 ** 31):
            result = - 2 ** 31
            
        return result