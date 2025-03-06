# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        # dummy node helps to simplify edge cases like if one of the lists is empty. Also provies starting point  for the new list
        tail = dummy  #tail is a reference to dummy. It will be used to build the merged list.

        while list1 and list2:   #the loop continues as long as both list1 and list2 have elements i.e not None
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next #moves list1 forward
            else:
                tail.next = list2
                list2 = list2.next #moves list2 forward
            
            tail = tail.next # tail is then moved forward to the newly added node.
        #If one list is exhausted while the other list still has remaining nodes, we simply connect tail.next to the non-empty list.
        tail.next = list1 if list1 else list2
        
        #We return dummy.next (not dummy itself) because dummy was just a placeholder
        return dummy.next

        

        