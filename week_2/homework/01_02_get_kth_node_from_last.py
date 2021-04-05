class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast =fast.next
        while fast is not None:
            fast= fast.next
            slow = slow.next
        return slow

    def print_all(self):
        print("모든 데이터")
        cur =self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.print_all()
print("=========================")


print(linked_list.get_kth_node_from_last(2).data)  #6
