'''
Runtime: 157 ms, faster than 11.64% of Python online submissions for Concatenation of Array.
Memory Usage: 14 MB, less than 5.50% of Python online submissions for Concatenation of Array.
'''

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_nums = [0 for i in range(len(nums)*2)]
        j = len(nums)
        for i in range(0, len(nums)):
            return_nums[i] = nums[i]
            return_nums[j] = nums[i]
            j = j + 1
        return return_nums


solution = Solution()
list = [1,3,5,2,6]
print(solution.getConcatenation(list))