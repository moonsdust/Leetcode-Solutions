class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        iterated = {}
        for num in nums: 
            if num in iterated: 
                return True 
            iterated[num] = 1
        return False