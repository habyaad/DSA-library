from collections import deque


class Stack:  # LIFO
    def __init__(self):
        self.stack = deque()

    def add(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def printStack(self):
        print(self.stack)

if __name__ == "__main__":
    newStack = Stack()
    newStack.add(5)
    newStack.add(50)
    newStack.add(500)
    newStack.printStack()
    print(newStack.size())
    print(newStack.pop())
    print(newStack.pop())
    print(newStack.pop())

    print(newStack.size())

    print(newStack.isEmpty())