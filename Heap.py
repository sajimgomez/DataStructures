class MinimumHeap :

    def __init__(self) :

        self.heap = []


    def get_min(self) :

        if len(self.heap) != 0 :

            return self.heap[0]

        print('There is no elements yet')

        return False


    def pop(self) :

        if len(self.heap) != 0 :

            self.heap[0] = self.heap[-1]

            self.heap = self.heap[:-1]

            self.bubble_down(0)

        else :

            print('There is no elements yet')

            return False


    def bubble_down(self, nodePosition) :

        leftChildPosition = 2 * nodePosition + 1

        rightChildPosition = leftChildPosition + 1

        smaller = nodePosition

        if self.is_valid(leftChildPosition) and self.heap[leftChildPosition] < self.heap[smaller] :

            smaller = leftChildPosition

        if self.is_valid(rightChildPosition) and self.heap[rightChildPosition] < self.heap[smaller] :

            smaller = rightChildPosition

        if smaller != nodePosition :

            self.swap_position(nodePosition, smaller)

            self.bubble_down(smaller)

       
    def is_valid(self, nodePosition) :

        if nodePosition <= len(self.heap) - 1 :

            return True

        return False


    def insert(self, node) :

        self.heap += [node]

        self.bubble_up(len(self.heap) - 1)


    def bubble_up(self, nodePosition) :

        # Visit papa, then compares if papa is smaller than son if it does, then nothing
        # else switch positions papa and son then call the same function until heap condition

        if nodePosition == 0 :

            return

        papaPosition = (nodePosition - 1) // 2

        if self.heap[papaPosition] > self.heap[nodePosition] :

            self.swap_position(papaPosition, nodePosition)

            self.bubble_up(papaPosition)


    def swap_position(self, pos1, pos2) :

        auxVar = self.heap[pos1]

        self.heap[pos1] = self.heap[pos2]

        self.heap[pos2] = auxVar


my_minHeap = MinimumHeap()

my_minHeap.insert(4)

my_minHeap.insert(50)

my_minHeap.insert(7)

my_minHeap.insert(55)

my_minHeap.insert(90)

my_minHeap.insert(87)

print(my_minHeap.heap)

print()

my_minHeap.insert(2)

print(my_minHeap.heap)

print()

print(my_minHeap.get_min())

print()

my_minHeap.pop()

print(my_minHeap.heap)

print()

my_minHeap.pop()

print(my_minHeap.heap)

my_minHeap.pop()

print()

print(my_minHeap.heap)

print()

my_minHeap.pop()

print(my_minHeap.heap)

my_minHeap.pop()

print()

print(my_minHeap.heap)

print()

my_minHeap.pop()

print(my_minHeap.heap)

print()

my_minHeap.pop()

print(my_minHeap.heap)

print()

my_minHeap.pop()

