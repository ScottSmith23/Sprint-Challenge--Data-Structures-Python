from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = DoublyLinkedList()
        self.cur = None

    def append(self, item):
        if self.capacity == len(self.data):
            self.cur.value = item

            if self.cur == self.data.tail:
                self.cur = self.data.head
            else:
                self.cur = self.cur.next
        else:
            self.data.add_to_tail(item)

            if len(self.data) == 1:

                self.cur = self.data.head
        

    def get(self):
        contents_list = []

        node = self.data.head
        while node is not None:
            contents_list.append(node.value)
            node = node.next

        return contents_list