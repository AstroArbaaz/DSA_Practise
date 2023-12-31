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
  
list = SinglyLinkedList()
list.append(4)
list.append(5)

print(list.head.data)
print(list.tail.data)
print(list._length)