class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(8)
n3 = Node(9)
n1.next = n2
n2.next = n3
head = n1
curr = head
dum = Node(0)
s = ''
while curr:
    s += str(curr.data)
    curr = curr.next
s = int(s) * 2
print(s)
for i in str(s):
    dum.next = Node(i)
    dum = dum.next
print(dum.data)

