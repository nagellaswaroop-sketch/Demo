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
n4.next = n5
n6 = Node(11)
head = n1
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
n6.next = slow.next
slow.next = n6
curr = head
while curr:
    print(curr.data)
    curr = curr.next  

