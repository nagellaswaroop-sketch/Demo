class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(8)
n2 = Node(7)
n3 = Node(15)
n4 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
head = n1
curr = head
c = head.data
# while curr:
#     if curr.data > c:
#         c = curr.data
#     curr = curr.next
# print(c)
while curr:
    if c > curr.data:
        c = curr.data
    curr = curr.next
print(c)
