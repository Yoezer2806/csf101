class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append data to the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    # 1. Method to find the middle element
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # 2. Method to detect if the list has a cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 3. Method to remove duplicates from an unsorted linked list
    def remove_duplicates(self):
        current = self.head
        prev = None
        seen_data = set()
        while current:
            if current.data in seen_data:
                prev.next = current.next
            else:
                seen_data.add(current.data)
                prev = current
            current = current.next

    # 4. Method to merge two sorted linked lists
    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy

        a = list1.head
        b = list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        # Attach the remaining nodes
        tail.next = a if a else b

        # Convert to LinkedList format
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# Test cases for the new methods

# Create and display a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5

# 1. Find the middle element
print("Middle element:", ll.find_middle())  # Output: 3

# 2. Check for cycle
print("Has cycle:", ll.has_cycle())  # Output: False

# Adding a cycle for testing
ll.head.next.next.next.next = ll.head.next  # Creates a cycle
print("Has cycle:", ll.has_cycle())  # Output: True

# Remove cycle to continue testing
ll.head.next.next.next.next = None

# 3. Remove duplicates
ll.append(3)  # Adding duplicate
ll.append(4)  # Adding duplicate
ll.display()  # Before removing duplicates
ll.remove_duplicates()
ll.display()  # After removing duplicates; Output should be: 1 -> 2 -> 3 -> 4 -> 5

# 4. Merge two sorted linked lists
ll1 = LinkedList()
ll2 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_list = LinkedList.merge_sorted(ll1, ll2)
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
