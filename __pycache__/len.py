class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(8)
n2 = Node(7)
n3 = Node(6)
n4 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
head = n1
curr = head
c = 0
while curr:
    c = c + 1
    curr = curr.next
print(c)   