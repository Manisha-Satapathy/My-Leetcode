class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1=str(x)
        newstr=str1[::-1]
        if(str1==newstr):
            return True
        else:
            return False
        