class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        dummy=x
        while dummy>0:
            r=dummy%10
            dummy=dummy//10
            rev=rev*10+r
        if x==rev:
            return True
        else:
            return False