# Node Class
class Node:
    # A Node class to represent each element in the list
    def __init__(self, data): # In the Python class you provided, self refers to the current instance of the class. It's a way for an object to refer to itself within its own methods.
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node, initialized as None


# Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0 # its not mandatory but generally it will help us to know the list length.


"""
Key Points about self:

Required for Instance Methods: All instance methods (methods that operate on a specific instance) must have self as their first argument.
Represents the Current Instance: self allows the method to access and modify the attributes and methods of the specific instance it's called on.
Not Used for Class Attributes: You don't need self to access class attributes (like i in this example) directly within the class, as they're shared by all instances.
Can Have Any Name: While self is the convention, you could use any valid variable name instead. However, using self is strongly recommended for clarity and consistency.
"""