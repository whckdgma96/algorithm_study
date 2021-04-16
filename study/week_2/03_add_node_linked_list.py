class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)  #[6]

        if index == 0:
            new_node.next =self.head
            self.head = new_node
            return

        node = self.get_node(index-1)  #[5]
        next_node = node.next       #[12]
        node.next = new_node        #[12자리에->6]
        new_node.next = next_node   #6다음자리에 12


# 5 12 8 3

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.append(3)


linked_list.add_node(1, 6)
#print(linked_list.get_node(0).data)
linked_list.print_all()
