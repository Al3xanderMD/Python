class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack elements:", stack.items)

    print("Peek:", stack.peek()) 
    print("Pop:", stack.pop())  

    print("Stack elements after pop:", stack.items)
    print("Is the stack empty?", stack.is_empty()) 
    print("Stack size:", stack.size())     
