class ListNode(object):
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next

lst1 = ListNode(2, ListNode(4, ListNode(3)))
lst2 = ListNode(1, ListNode(2, ListNode(3)))

stack_num1 = []
stack_num2 = []

while lst1:
    stack_num1.append(lst1.key)
    lst1 = lst1.next

while lst2:
    stack_num2.append(lst2.key)
    lst2 = lst2.next

num1 = 0
num1 += stack_num1.pop() * 100
num1 += stack_num1.pop() * 10
num1 += stack_num1.pop()
print(num1, end=" ")


num2 = 0
num2 += stack_num2.pop() * 100
num2 += stack_num2.pop() * 10
num2 += stack_num2.pop()
print(num2, end=" ")

sum = num1 + num2

str = str(sum)
stack_sum = []
for d in str:
    stack_sum.append(d)

result = ListNode(stack_sum.pop(), ListNode(stack_sum.pop(), ListNode(stack_sum.pop())))

print("")
print(result)