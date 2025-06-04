class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev



class DoublyLinked:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def add_to_tail(self, value):
        tail = self.head
        while tail.next:
            tail = tail.next

        new_node = Node(value, None, tail)
        tail.next = new_node

    def print_list(self):
        print("\n[", end="")
        head = self.head
        while head:
            print(f"'{head.value}'", end=", ")
            head = head.next
        print("]\n")

    def get_length(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count

    def insert_after_index(self, value, index):
        if self.get_length() - 1 < index:
            print("out of range")
            return

        count = 0
        curr_node = self.head
        while count != index:
            curr_node = curr_node.next
            count += 1

        new_node = Node(value, curr_node.next, curr_node)
        curr_node.next = new_node


doubly = DoublyLinked()

doubly.add_to_head("first")
doubly.add_to_head("second")
doubly.add_to_head("third")
doubly.add_to_head("fourth")
# print(doubly.get_length())
doubly.insert_after_index("inserted after index 2", 3)
# doubly.add_to_tail("third")
doubly.print_list()

# node1 = {
#     "value": "1",
#     "next": None,
#     "prev": node1
# }
# node2 = {
#     "value": "2",
#     "next": node1,
#     ""
# }
# [node2, node1]
