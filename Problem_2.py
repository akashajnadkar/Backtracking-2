#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []
    
    def isPallindrome(self, s): #check if the string is pallindrome or not
        left, right = 0, len(s)-1
        while left<right:
            if s[left] !=s[right]:
                return False
            left+=1
            right-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        self.helper(s, 0, [])
        return self.result

    # for loop recusrion
    
    def helper(self, s, pivot, path):
        #base
        if pivot == len(s): #if my pivot reaches the length of the string then append the strings in the path to my result
            self.result.append(path[:])
            return
        #logic
        for i in range(pivot, len(s)): #for every character from pivot to end
            if self.isPallindrome(s[pivot:i+1]):#if the substring between pivot and i is pallindrome 
                path.append(s[pivot:i+1]) #append the string to the path
                self.helper(s, i+1, path) #find the next scenario with pivot at i+1
                path.pop() #remove the appended string from the current path, to obtain future scenarios

    # 0/1 recursion
    # def helper(self, s, pivot, i, path, cnt):
    #     #base
    #     if i ==len(s):
    #         print(path," ", cnt)
    #         if cnt == len(s):
    #             self.result.append(path[:])
    #         return

    #     #logic
    #     #don't choose
    #     self.helper(s, pivot, i+1, path, cnt)

    #     #choose
    #     currSub = s[pivot:i+1]
    #     if self.isPallindrome(currSub):
    #         #action
    #         path.append(currSub)
    #         #recurse
    #         self.helper(s, i+1, i+1, path, cnt + len(currSub))
    #         #backtrack
    #         path.pop()



        
# @lc code=end

