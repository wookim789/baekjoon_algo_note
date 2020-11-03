# 문자열 지그 재그로 출력하기
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[] for i in range(numRows)]
        n = numRows
        
        idx = 0
        is_up = True
        for c in s:
            if 0 <= idx < n:
                arr[idx].append(c)
                if is_up:
                    idx += 1
                else: 
                    idx -= 1
            else:
                if is_up:
                    is_up = False
                    idx -= 2
                    arr[idx].append(c)
                    idx -= 1
                else:
                    is_up = True
                    idx += 2
                    arr[idx].append(c)
                    idx += 1
        result = ""
        for i in arr:
            result += ''.join(i)
        return result