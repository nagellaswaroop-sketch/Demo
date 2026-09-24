class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(8)
n2 = Node(7)
n3 = Node(15)
n4 = Node(9)
n5 = Node(10)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1
head = n1
curr = head

while curr.next != head:
    curr = curr.next

n5.next = head
curr.next = n5
head = n5
    