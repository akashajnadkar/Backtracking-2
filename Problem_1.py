#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start

'''
Time Complexity - O(2^n) since we are using backtracking. As for every number in the list we have 2 options
Space Complexity - O(n) recursive stack space

This code works on Leetcode
'''
class Solution:
    def __init__(self):
        self.result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0, [])
        return self.result
    
    def helper(self, nums, idx, path):
        self.result.append(path[:]) #append the path to result once we reach the end of set
        for i in range(idx, len(nums)):
            path.append(nums[i]) #if i choose to take the number i the path
            self.helper(nums, i+1, path) #future scenarios if i take the number in the path
            path.pop() #if i dont want the number in the path
        
# @lc code=end

