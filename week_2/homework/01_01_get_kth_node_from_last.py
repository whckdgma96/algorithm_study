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

    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1

        print("길이는", length)
        print("=================================")

        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next

        return cur


# 1 2 3 4 5 6
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
