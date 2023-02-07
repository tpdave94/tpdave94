class Node:
    """Node Implementation."""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Stack(LIFO) Implementation."""

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        """Push the element into stack."""
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def is_empty(self):
        """Return True is stack is empty else False."""
        if self.head:
            return True
        return False

    def pop(self):
        """Remove Last element."""
        if not self.is_empty():
            raise Exception("Stack is empty.")
        pop_item_node = self.head
        self.head = pop_item_node.next
        self.size -= 1
        return pop_item_node.value

    def __str__(self):
        """Representation of stack."""
        last_node = self.head
        output = ""
        while last_node:
            output += str(last_node.value) + "->"
            last_node = last_node.next
        return output[:-2]


stack_obj = Stack()
for i in range(1, 5):
    stack_obj.push(i)

print(stack_obj)
print('POP: ', str(stack_obj.pop()))
print(stack_obj)
