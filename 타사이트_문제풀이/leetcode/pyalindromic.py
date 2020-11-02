class Solution(object):
    def longestPalindrome(self, s):
        result = []
        n = len(s)
        if n == 1:
            return s
        for i in range(n):
            cur_s = s[i]
            for j in range(i + 1, n):
                result = self.check_paindromic(cur_s, result)
                cur_s += s[j]
            result = self.check_paindromic(cur_s, result)
        return result[-1]
    
    def check_paindromic(self, s, result):
        if s in result:
            return result
        n = len(s) - 1
        l = (len(s) / 2)
        if l <= 0:
            l = 1
        for i in range(l):
            if s[i] != s[n - i]:
                return result
        if not result or len(s) > len(result[-1]):
            result.append(s)
        return result
