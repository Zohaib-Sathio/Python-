'''
Runtime: 147 ms, faster than 64.55% of Python online submissions for Build Array from Permutation.
Memory Usage: 13.6 MB, less than 58.71% of Python online submissions for Build Array from Permutation.
'''
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_nums = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            return_nums[i] = nums[nums[i]]
        return return_nums


solution = Solution()
list = [1,2,4,5,3,0]
return_list = solution.buildArray(list)
print(return_list)