class Node:
    """Node Implementation."""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Stack(LIFO) Implementation."""

    def __init__(self):
        self.head = Node('Head')
        self.size = 0

    def push(self, value):
        """Push the element into stack."""
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def is_empty(self):
        """Return True is stack is empty else False."""
        if self.head.next:
            return True
        return False

    def pop(self):
        """Remove Last element."""
        if self.is_empty():
            raise Exception("Stack is empty.")
        pop_item_node = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return pop_item_node.value

    def __str__(self):
        """Representation of stack."""
        last_node = self.head.next
        output = ""
        while not last_node:
            output += str(last_node.value) + "->"
            last_node = last_node.next
        return output[:-2]


stack_obj = Stack()
for i in range(1, 5):
    stack_obj.push(i)

print(stack_obj)
print(stack_obj.pop())
