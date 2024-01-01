class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None


class SinglyLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self._length = 0

  def append(self, value):
    new_node = Node(value)
    if not self._length:
      self.head = self.tail = new_node # If list is empty, new node becomes the head and tail
    else:
      self.tail.next = new_node
      self.tail = new_node
    self._length += 1
    return self
  
  def prepend(self, value):
    new_node = Node(value)
    if not self._length:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self._length += 1
    return self
  
  # pop head - to remove head
  def pophead(self):
    if not self._length:
      raise Exception("list is empty")
    old_head = self.head  # Store the old head
    self.head = old_head.next  # Update the head to the next node
    old_head.next = None  # Disconnect the old head from the list
    self._length -= 1  # Decrement the length
    if not self._length:
      self.tail = None
    return old_head.data

  
list = SinglyLinkedList()

list.append(5)
list.append(7)
list.prepend(8)
# list.pophead()


print(list.head.data)
print(list.tail.data)
print(list._length)