class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xc = str(x)
        backwards = xc[len(xc)::-1]
        if xc == backwards: 
            return True 
        return False