class Node :

    def __init__(self, value, next = None) :

        self.value = value

        self.next = next


class LinkedList :

    def __init__(self) :

        self.head = None

        self.tail = None

    
    def AddToBeginning(self, node) :

        if self.head == None and self.tail == None :

           self.tail = node 

           self.head = node

        else :   

            node.next = self.head

            self.head = node


    def AddToEnd(self, node) :

        if self.head == None and self.tail == None :

           self.tail = node 

           self.head = node

        else :   

            # head-->1<--tail  2
            # 
            self.tail.next = node

            self.tail = node


    # Search if position exists
    # if exists, then go to the previous, then set previous next equal to previous next next
    # else print position doesn't exists, try another smaller position

    # 1-->2-->3-->None

    def ExistPosition(self, position) :

        Pointer = self.head

        ExistPosition = True

        for i in range(1, position + 1) :

            if Pointer != None :

                Pointer = Pointer.next

            else :

                ExistPosition = False

        return ExistPosition


    def DeleteNode(self, position) :

        if self.ExistPosition(position) :

            if position > 1 :

                Pointer = self.head

                for i in range(1, position - 1) :

                    Pointer = Pointer.next

                Pointer.next = Pointer.next.next

            elif position == 1 :

                Pointer = self.head

                self.head = Pointer.next

            else :

                print('Position starts with 1')

        else :

            print('Try another smaller position')


    def PrintNodes(self) :

        node = self.head

        while node != None :

            print(node.value)

            node = node.next


n1 = Node(1)

n2 = Node(2)

n3 = Node(3)

n4 = Node(4)

l1 = LinkedList()

l1.AddToBeginning(n1)

l1.AddToEnd(n2)

l1.AddToBeginning(n3)

l1.AddToEnd(n4)

l1.PrintNodes()

# 3-->1-->2-->4
# Delete position = 3, (2)
print()

l1.DeleteNode(5)

l1.PrintNodes()

