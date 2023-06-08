#implementation of doubly link list

#-------implementation of node class------
class Node:
    head = None
    tail = None
    def __init__(self, data):
        self.key = data
        self.prev = None
        self.next = None

#--------Insert function-------------
def insert(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.tail = Node.head
    else:
        temp = Node(data)
        temp.prev = Node.tail
        Node.tail.next = temp
        Node.tail = temp

#---------Insert at begin----------------
def insert_at_begin(data):
    if Node.head == None:
        insert(data)
    else:
        temp = Node(data)
        temp.next = Node.head
        Node.head.prev = temp
        Node.head = temp

#--------Inser at a position------------
def insert_at_pos(data, pos):
    if Node.head == None:
        print("wrong position")
    elif pos == 1:
        insert_at_begin(data)
    else:
        temp = Node(data)
        curr = Node.head
        for index in range(pos - 2):
            curr = curr.next
            if curr == None:
                print("wrong position")
                return
        temp.next = curr.next
        temp.prev = curr
        curr.next = temp  

#--------delete a node---------------------
def delete():
    if Node.head == None:
        print("Nothing to delete")
    else:
        Node.tail = Node.tail.prev
        Node.tail.next = None

#---------delete at begin-------------------
def delete_first():
    if Node.head == None:
        print("Nothing to delete")
    else:
        Node.head = Node.head.next
        Node.head.prev = None

#--------delete at pos----------------------
def delete_at_pos(pos):
    if Node.head == None:
        print("wrong pos")
    elif pos == 1:
        delete_first()
    else:
        curr = Node.head
        for index in range(pos - 2):
            curr = curr.next
        nextNode = curr.next.next
        curr.next = nextNode
        if curr.next != None:
            nextNode.prev = curr

#---------traverse function-----------------
def traverse():
    if Node.head == None:
        return
    else:
        curr = Node.head
        while curr != None:
            print(curr.key)
            curr = curr.next

#---------search a node----------------------
def search(data):
    index = 0
    if Node.head == None:
        print("List is empty")
    else:
        curr = Node.head
        while curr != None:
            index += 1
            if curr.key == data:
                print(index)
                return
            curr = curr.next
        if curr.next == Node.head:
            print("-1")

#-------reverse the doubly link list---------
def reverse():
    if Node.head == None:
        return
    if Node.head.next == None:
        return
    else:
        stack = []
        curr = Node.head
        Node.head = None

        while curr is not None:
            stack.append(curr.key)
            curr = curr.next

        while len(stack) > 0:
            insert(stack.pop())


insert(10)
insert(20)
insert(30)
insert(40)
insert(50)
insert(60)
delete_at_pos(6)
traverse()
reverse()
traverse()