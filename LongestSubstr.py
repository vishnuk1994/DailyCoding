# Given a string, find the length of the longest substring without repeating characters.

import timeit

class Solution:
  def lengthOfLongestSubstring_linear(self, s):
    n = len(s)
    max_len = 1
    cur_len = 1
    prev_ind = 0
    visited = [-1] * 256
    visited[ord(s[0])] = 0
    for i in range(1,n):
        prev_ind = visited[ord(s[i])]
        
        if prev_ind == -1 or (i-cur_len > prev_ind):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev_ind
            
        visited[ord(s[i])] = i
    if cur_len > max_len:
        max_len = cur_len
    return max_len

  def lengthOfLongestSubstring(self, s):
        substr = ""
        max_len = 0
        for i in s:
            if i not in substr:
                substr += i
            else:
                l = len(substr)
                if l > max_len:
                    max_len = l
                substr = ""
        return max_len
       
# ideally the code with linear approach should work better as compared to 2nd approach
# but when measured using timeit 2nd approach is actually fater than 1st one
string = "abrkaabcdefghijjxxx"
print(Solution().lengthOfLongestSubstring(string))

# below code for testing the time
lameSetp = '''
class Solution:
  def lengthOfLongestSubstring(self, s):
    substr = ""
    max_len = 0
    for i in s:
        if i not in substr:
            substr += i
        else:
            l = len(substr)
            if l > max_len:
                max_len = l
            substr = ""
    return max_len
'''

advSetp = '''
class Solution:
  def lengthOfLongestSubstring(self, s):
    n = len(s)
    max_len = 1
    cur_len = 1
    prev_ind = 0
    visited = [-1] * 256
    visited[ord(s[0])] = 0
    for i in range(1,n):
        prev_ind = visited[ord(s[i])]
        
        if prev_ind == -1 or (i-cur_len > prev_ind):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev_ind
            
        visited[ord(s[i])] = i
    if cur_len > max_len:
        max_len = cur_len
    return max_len
''' 

stmt = '''
string = 'abrkaabcdefghijjxxxinowevffffegweoifgoiwegoweigioe'
newStr = ""
for _ in range(1000):
    newStr += string
Solution().lengthOfLongestSubstring(newStr)
'''
#print(timeit.timeit(setup=lameSetp,stmt=stmt,number=10))
#print(timeit.timeit(setup=advSetp,stmt=stmt,number=10))
