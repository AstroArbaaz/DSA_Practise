package main

import "fmt"

// Node Struct
type Node struct {
    Data int   // The data stored in the node
    Next *Node // Pointer to the next node, initialized as nil (Go's equivalent of Python's None)
}

// SinglyLinkedList Struct
type SinglyLinkedList struct {
    Head   *Node // The head of the list
    Tail   *Node // The tail of the list
    Length int   // The length of the list
}

// NewNode creates a new node with the given data
func NewNode(data int) *Node {
    return &Node{Data: data}
}

// Append method adds a new node at the end of the list
func (list *SinglyLinkedList) Append(data int) {
    newNode := NewNode(data)
    if list.Length == 0 {
        list.Head = newNode // If list is empty, new node becomes the head
        list.Tail = newNode // And also the tail
    } else {
        list.Tail.Next = newNode // Set the next of the last node to new node
        list.Tail = newNode      // Update the tail to the new node
    }
    list.Length++ // Increment the length
}

// prepend
func (list *SinglyLinkedList) prepend(data int) {
    newNode := NewNode(data)
    if list.Length == 0 {
        list.Head = newNode // If list is empty, new node becomes the head
        list.Tail = newNode // And also the tail
    } else {
        newNode.Next = list.Head
        list.Head = newNode
    }
    list.Length++ // Increment the length
}

// Main function to demonstrate usage
func main() {
    list := &SinglyLinkedList{}
    list.Append(4)
    list.Append(5)
    list.prepend(4)
    list.prepend(6)

    fmt.Println(list.Head.Data)  // Output: 4
    fmt.Println(list.Tail.Data)  // Output: 5
    fmt.Println(list.Length)     // Output: 2
}