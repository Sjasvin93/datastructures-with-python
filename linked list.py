#----------class Node to create the linked list----------
class Node:
    head = None
    tail = None
    def __init__(self, data):
        self.key = data
        self.next = None

#-------delete first element from the list-----------
def delete_first():
    if Node.head == None:
        return
    else:
        Node.head = Node.head.next

#-------delete the last element from the list----------
def delete_last():
    if Node.tail == Node.head:
        Node.tail, Node.head = None
    else:
        curr = Node.head
        while curr.next != Node.tail:
            curr = curr.next
        Node.tail = curr
        Node.tail.next = None

def delete_at_pos(pos):
    if pos == 1:
        delete_first()
        return
    else:
        curr = Node.head
        for i in range(pos - 2):
            curr = curr.next
            if curr == None:
                return
        curr.next = curr.next.next

#---------insert at the begining-----------
def insert_at_begin(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.tail = Node.head
    else:
        temp = Node(data)
        temp.next = Node.head
        Node.head = temp

#--------inserting in the linked list----------
def insert(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.tail = Node.head
    else:
        Node.tail.next = Node(data)
        Node.tail = Node.tail.next

def sorted_insert(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.tail = Node.head
    else:
        if data < Node.head.key:
            insert_at_begin(data)
        elif data > Node.tail.key:
            insert(data)
        else:
            temp = Node(data)
            curr = Node.head.next
            prev = Node.head
            while data >= curr.key:
                prev = curr
                curr = curr.next
            temp.next = curr
            prev.next = temp
            
#----------insert at position---------
def insert_at_pos(pos, data):
    if pos == 1:
        insert_at_begin(data)
        return
    else:
        curr = Node.head
        for index in range(pos - 2):
            curr = curr.next
            if curr == None:
                return Node.head
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

#-----Reverse the linked list---------
def reverse_link_list():
    curr = Node.head
    stack = []

    while curr is not None:
        stack.append(curr.key)
        curr = curr.next

    curr = Node.head
    while curr is not None:
            curr.key = stack.pop()
            curr = curr.next

    return Node.head

#--------Traverse the linked list--------
def traverse_list():
    if Node.head == None:
        return None
    
    curr = Node.head
    while curr != None:
        print(curr.key)
        curr = curr.next

#--------Search an element in the list--------
def search(element):
    pos = 1
    if Node.head == None:
        print("List is empty")
        return
    else:
        curr = Node.head
        while curr != None:
            if curr.key == element:
                print(pos)
                return
            curr = curr.next
            pos += 1
    print(-1)

#-----Creating the linked list-----
sorted_insert(20)
sorted_insert(10)
sorted_insert(50)
sorted_insert(40)
sorted_insert(30)
sorted_insert(60)
traverse_list()