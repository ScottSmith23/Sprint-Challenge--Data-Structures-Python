"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        nodeValue = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = nodeValue
            self.tail = nodeValue
        else:
            nodeValue.next = self.head
            self.head.prev = nodeValue
            self.head = nodeValue
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        headValue = self.head.value
        self.delete(self.head)
        return headValue
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        nodeValue = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = nodeValue
            self.tail = nodeValue
        else:
            nodeValue.prev = self.tail
            self.tail.next = nodeValue
            self.tail = nodeValue
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tailValue = self.tail.value
        self.delete(self.tail)
        return tailValue
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        nodeValue = node.value
        self.delete(node)
        self.add_to_head(nodeValue)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        nodeValue = node.value
        self.delete(node)
        self.add_to_tail(nodeValue)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #list is empty
        if not self.head and not self.tail:
            pass
        self.length -=1
        #list has only 1 value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #if node is head
        elif self.head == node:
            self.head = self.head.next
        #if node is tail    
        elif self.tail == node:
            self.tail = self.tail.prev
            


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        maxVal = self.head.value
        curVal = self.head
        while curVal:
            if curVal.value > maxVal:
                maxVal = curVal.value
            curVal = curVal.next
        return maxVal
