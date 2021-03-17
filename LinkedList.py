from Node import Node


class LinkedList:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.size = 0
        self.head = Node(None, None)
        self.tail = Node(None, self.head)
        for elem in arr:
            self.append(elem)

    def append(self, elem):
        last_node = self.tail.link
        new_node = Node(elem)
        last_node.set_link(new_node)
        self.tail.set_link(new_node)
        self.size += 1

    def push_front(self, elem):
        if self.head.link is None:
            self.append(elem)
        else:
            new_node = Node(elem, self.head.link)
            self.head.set_link(new_node)
            self.size += 1

    def delete_front(self):
        if self.head.link is None:
            raise Exception('Cannot delete from an empty linked list')

        self.head.set_link(self.head.link.link)
        self.size -= 1

    def pop(self):
        if self.head.link is None:
            raise Exception('Cannot pop from an empty linked list')

        previous_node = self.head
        current_node = self.head.link

        while current_node.link is not None:
            previous_node = current_node
            current_node = current_node.link

        previous_node.set_link(None)
        self.tail.set_link(previous_node)
        self.size -= 1

    def print(self):
        arr = []
        current_node = self.head

        while True:
            if current_node.data is not None:
                arr.append(current_node.data)
            if current_node.link is None:
                break
            current_node = current_node.link

        print(arr)

    def get(self, index):
        if index >= self.size:
            raise Exception('Linked List Index Out of Bounds')

        current_node = self.head
        for _ in range(index+1):
            current_node = current_node.link

        return current_node.data
