#------Node class---------
class Node:
    head = None
    tail = None
    def __init__(self, data):
        self.key = data
        self.next = None

#--------Insert function--------
def insert(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.head.next = Node.head
        Node.tail = Node.head
        Node.tail.next = Node.head
    else:
        temp = Node(data)
        temp.next = Node.head
        Node.tail.next = temp
        Node.tail = temp

#--------Insert at begin-------------
def insert_at_begin(data):
    if Node.head == None:
        Node.head = Node(data)
        Node.head.next = Node.head
        Node.tail = Node.head
    else:
        temp = Node(data)
        temp.next = Node.head
        Node.tail.next = temp
        Node.head = temp

#-------Insert at pos-------------------
def insert_at_pos(pos, data):
    if pos == 1:
        insert_at_begin(data)
    else:
        curr = Node.head
        for index in range(pos - 2):
            curr = curr.next
            if curr.next == Node.head:
                print("Insert index out of range")
                return
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

#--------Traverse the list---------------
def traverse_list():
    if Node.head == None:
        print("List is empty")
    elif Node.head.next == Node.head:
        print(Node.head.key)
    else:
        print(Node.head.key)
        curr = Node.head.next
        while curr != Node.head:
            print(curr.key)
            curr = curr.next            

#--------Delete the first Node-------------
def delete_first():
    if Node.head == None:
        print("Nothing to delete")
    elif Node.head.next == Node.head:
        Node.head = None
        Node.tail = None
    else:
        Node.tail.next = Node.head.next
        Node.head = Node.head.next

#----------Delete last Node----------------
def delete_last():
    if Node.head == None:
        print("Nothing to delete")
    elif Node.head.next == Node.head:
        Node.head = None
        Node.tail = None
    else:
        curr = Node.head
        while curr.next != Node.tail:
            curr = curr.next
        curr.next = Node.head

#----delete at position--------------------
def delete_at_pos(pos):
    if Node.head == None or pos < 1:
        print("Nothing to delete")
    elif pos == 1:
        delete_first()
    else:
        curr = Node.head
        for index in range(pos - 2):
            curr = curr.next
            if curr.next == Node.head:
                print("Wrong position index out of range")
                return    
        curr.next = curr.next.next

#----------sorted insert--------------
def sorted_insert(data):
    if Node.head == None:
        insert(data)
    elif Node.head.key > data:
        insert_at_begin(data)
    elif Node.tail.key > data:
        insert(data)
    else:
        print("I reached here", data)
        temp = Node(data)
        prev = Node.head
        curr = Node.head.next
        while curr.key < data:
            prev = curr
            curr = curr.next
        temp.next = curr
        prev.next = temp

sorted_insert(30)
sorted_insert(20)
sorted_insert(90)
sorted_insert(40)
sorted_insert(55)
sorted_insert(10)
print("hello")
traverse_list()