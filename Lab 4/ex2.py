class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print("Queue elements:", queue.items)

    print("Peek:", queue.peek())  
    print("Pop:", queue.pop())   

    print("Queue elements after pop:", queue.items)
    print("Is the queue empty?", queue.is_empty())  
    print("Queue size:", queue.size())     
