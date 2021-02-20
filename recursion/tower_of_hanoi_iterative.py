
class Stack(object):
    def __init__(self, capacity=0, top=0, array=[]):
        self.capacity = capacity
        self.top = top
        self.array = array

    def is_full(self):
        '''
        Stack is full when the top is equal to the last index.
        :param stack:
        :return:
        '''
        return (self.top == self.capacity - 1)

    def is_empty(self):
        return (len(self.array) == 0)


    def push(self, item):
        '''
        Add an item to the stack and increase
        top by 1
        :param item:
        :return:
        '''
        if self.is_full():
            return

        self.top += 1
        self.array.append(item)


    def pop(self):
        if self.is_empty():
            return 0

        self.top -= 1
        return self.array.pop()

class TOH(object):

    def __init__(self, stack=None):
        self.stack = stack

    def createStack(self, capacity):
        stack = Stack()
        stack.capacity = capacity
        stack.top = -1
        stack.array = []
        return stack


    def move_disk_between_two_poles(self, src, dest, s, d):
        pole1_top_disk = src.pop()
        pole2_top_disk = dest.pop()

        if pole1_top_disk == 0:
            src.push(pole2_top_disk)
            self.move_disk(d, s, pole2_top_disk)
        elif pole1_top_disk > pole2_top_disk:
            src.push(pole1_top_disk)
            src.push(pole2_top_disk)
            self.move_disk(d, s, pole2_top_disk)
        else:
            dest.push(pole2_top_disk)
            dest.push(pole1_top_disk)
            self.move_disk(s, d, pole1_top_disk)


    def move_disk(self, from_peg, to_peg, disk):
        '''
        Show the movement of the disks between pegs
        :param from_peg:
        :param to_peg:
        :param disk:
        :return:
        '''
        print(f"Move the disk {disk} from {from_peg} to {to_peg}")


    def tower_of_hanoi(self, num_of_disks, src, aux, dest):
        '''
        1. Calculate the total number of moves required ie pow(2, n)
        2. If number of disks (ie n) is even then interchange destination
        pole and auxiliary.
        3. for i = 1 to total number of moves:
            if i%3 == 1:
                legal movement of top disk between source pole and destination pole
            if i%3 == 2:
                legal movement of top disk between source pole and destination pole
            if i%3 == 0:
                legal movement top disk between auxiliary pole and destination pole
        '''
        s, d, a = 'S', 'D', 'A'

        '''
        If number of disks is even, then
        interchange destination pole and
        auxiliary pole.
        '''
        if num_of_disks % 2 == 0:
            temp = d
            d = a
            a = temp

        total_num_of_moves = pow(2, num_of_disks) - 1

        # Larger disks will be pushed first
        for i in range(num_of_disks, 1, -1):
            src.push(i)

        for i in range(1, total_num_of_moves):
            if i % 3 == 1:
                self.move_disk_between_two_poles(src, dest, s, d)
            elif i % 3 == 2:
                self.move_disk_between_two_poles(src, aux, s, a)
            elif i % 3 == 0:
                self.move_disk_between_two_poles(aux, dest, a, d)

# Driver
num_of_disks = 3

ob = TOH()
src = ob.createStack(num_of_disks)
dest = ob.createStack(num_of_disks)
aux = ob.createStack(num_of_disks)

ob.tower_of_hanoi(num_of_disks, src, aux, dest)
