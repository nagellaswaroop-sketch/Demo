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
head = n1
curr = head
l = []
while curr:
    l.append(curr.data)
    curr = curr.next
if l == l[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
