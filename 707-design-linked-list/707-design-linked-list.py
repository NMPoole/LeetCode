class Node(object):
    next = None
    data = None
    prev = None

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class MyLinkedList(object):
    head = None
    tail = None
    size = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.data

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        nodeToAdd = Node(val)

        if self.size == 0:
            nodeToAdd.next = None
            self.tail = nodeToAdd
        else:
            nodeToAdd.next = self.head
            self.head.prev = nodeToAdd

        nodeToAdd.prev = None
        self.head = nodeToAdd

        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        nodeToAdd = Node(val)

        if self.size == 0:
            nodeToAdd.prev = None
            self.head = nodeToAdd
        else:
            nodeToAdd.prev = self.tail
            self.tail.next = nodeToAdd

        nodeToAdd.next = None
        self.tail = nodeToAdd

        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            nodeToAdd = Node(val)

            prevNode = self.head
            for _ in range(index - 1):
                prevNode = prevNode.next
            nextNode = prevNode.next

            nodeToAdd.prev = prevNode
            nodeToAdd.next = nextNode
            prevNode.next = nodeToAdd
            nextNode.prev = nodeToAdd

            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        currNode = self.head
        for _ in range(index):
            currNode = currNode.next

        if self.size == 1:
            self.head = None
            self.tail = None
        elif currNode is self.head:
            currNode.next.prev = currNode.prev
            self.head = currNode.next
        elif currNode is self.tail:
            currNode.prev.next = currNode.next
            self.tail = currNode.prev
        else:
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev

        self.size -= 1


            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)