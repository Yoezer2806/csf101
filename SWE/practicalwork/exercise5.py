class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# 1. Evaluate postfix expression using a stack
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            right = stack.pop()
            left = stack.pop()
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left / right)
    return stack.pop()

# Test evaluate_postfix
print(evaluate_postfix("53+82-*"))  # Example: should print -3

# 2. Implement a queue using two stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")

# Test QueueWithStacks
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1

# 3. Task scheduler using a queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

def task_scheduler(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)
    
    while not queue.is_empty():
        current_task = queue.dequeue()
        print(f"Processing task: {current_task}")

# Test task_scheduler
tasks = ["Task 1", "Task 2", "Task 3"]
task_scheduler(tasks)

# 4. Convert infix to postfix using a stack
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    output = ""
    for char in expression:
        if char.isalnum():  # if operand, add to output
            output += char
        elif char == '(':  # if '(', push to stack
            stack.push(char)
        elif char == ')':  # if ')', pop until '('
            while not stack.is_empty() and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:  # operator
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                output += stack.pop()
            stack.push(char)
    while not stack.is_empty():  # pop all operators left in stack
        output += stack.pop()
    return output

# Test infix_to_postfix
print(infix_to_postfix("A+B*(C^D-E)"))  # Example: should print "ABCD^E-*+"
