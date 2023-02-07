class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if not self.size:
            self.start = node
            self.end = node
        else:
            node.next = None
            self.end.next = node
            self.end = node
        self.size += 1

    def is_empty(self):
        """Return True is Queue is empty else False."""
        if not self.size:
            return True
        return False

    def dqueue(self):
        if self.is_empty():
            raise Exception("Queue is Empty.")
        dqueue_node = self.start
        self.start = dqueue_node.next
        return dqueue_node.value

    def __str__(self):
        head = self.start
        output = ""
        while head:
            output += str(head.value) + '->'
            head = head.next
        return output[:-2]


queue_obj = Queue()
for i in range(1, 5):
    queue_obj.enqueue(i)
print(queue_obj)
print("Dqueue: ", queue_obj.dqueue())
print(queue_obj)