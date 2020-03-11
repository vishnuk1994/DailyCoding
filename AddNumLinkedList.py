'''
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    res = ListNode(-1)
    sum = 0
    carry = 0
    t = res
    while l1 and l2:
        sum = l1.val + l2.val + carry
        carry = 0
        if sum > 9:
            carry = 1
    
        #print("sum is {}".format(sum))
        if res.val == -1:
            res = ListNode(sum%10);
            t = res
        else:
            while t.next:
                t = t.next
            #print("sum is {}".format(sum))
            t.next = ListNode(sum%10);
        l1 = l1.next
        l2 = l2.next
    
    #print("l1 : {} , l2 : {}".format(l1,l2)) 
    if l1 or l2:
        #print("here")
        if l1:
            l3 = l1
        else:
            l3 = l2
            
        while l3:
            sum = l3.val + carry
            #print("sum is {}".format(sum))
            carry = 0
            if sum > 9:
                carry = 1
           
            while t.next:
                t = t.next
            t.next = ListNode(sum%10);
            
            l3 = l3.next
            
    if carry == 1:
        while t.next:
            t = t.next
        t.next = ListNode(1);
                
    return res

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
#trying out with more digits
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
