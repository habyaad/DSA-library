class Node:
    def __init__(self, nData, prevN, nextN):
        self.nodeData = nData
        self.prevNode = prevN
        self.nextNode = nextN


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

# insertion processes
    def insertAtBeginning(self, newData):
        if self.head is None:
            node = Node(newData, None, self.head)
            self.head = node
        else:
            self.head.prevNode = Node(newData, None, self.head)
            self.head = self.head.prevNode
        self.length += 1

    def insertAtEnd(self, newData):
        if self.head is None:
            node = Node(newData, None, self.head)
            self.head = node
        else:
            itr = self.head
            while itr is not None:
                if itr.nextNode == None:
                    itr.nextNode = Node(newData, itr, None)
                    break
                else:
                    itr = itr.nextNode
        self.length += 1

    def insertValues(self, newValues):
        for data in newValues:
            self.insertAtEnd(data)

    def insertAt(self, index, newData):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")
        elif index == 0:
            self.insertAtBeginning(newData)
        else:
            itr = self.head
            count = 0
            while itr is not None:
                if count == index-1:
                    node = Node(newData, itr, itr.nextNode)
                    itr.nextNode.prevNode = node
                    itr.nextNode = node
                    self.length += 1
                    break

                count += 1
                itr = itr.nextNode

    # deletion processes
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.nextNode
            self.head.prevNode = None
            self.length -= 1

        else:
            itr = self.head
            count = 0
            while itr is not None:
                if count == index-1:
                    itr.nextNode = itr.nextNode.nextNode
                    itr.nextNode.prevNode = itr
                    self.length -= 1
                    break
                itr = itr.nextNode
                count += 1

    def remove(self, value):
        if self.exists(value):
            itr = self.head
            last_item = self.getLastItem()
            # if item is first
            if itr.nodeData == value:
                self.head = self.head.nextNode
                self.head.prevNode = None
                self.length -= 1
            # if item is last
            elif last_item.nodeData == value:
                while itr is not None:

                    if itr.nextNode.nextNode == None:
                        itr.nextNode = None

                        self.length -= 1
                        break
                    itr = itr.nextNode
            else:
                while itr is not None:

                    if itr.nextNode.nodeData == value:
                        itr.nextNode = itr.nextNode.nextNode
                        itr.nextNode.prevNode = itr
                        self.length -= 1
                        break
                    itr = itr.nextNode
        else:
            raise Exception(f"{value} does not exist in the doubly linked list")

    # extras
    def count(self, value) -> int:
        itr = self.head
        count = 0
        while itr is not None:
            if itr.nodeData == value:
                count += 1
            itr = itr.nextNode
        return count

    def exists(self, value) -> bool:
        return True if self.count(value) > 0 else False

    def index(self, value) -> int:
        itr = self.head
        count = 0
        if self.exists(value):
            while itr is not None:
                if itr.nodeData == value:
                    return count
                itr = itr.nextNode
                count += 1
        else:
            raise Exception(f"{value} does not exist in doubly linked list")

    def getLastItem(self) -> Node:
        itr = self.head
        if itr is None:
            return itr
        else:
            while itr.nextNode is not None:
                itr = itr.nextNode
            return itr

    def getLength(self) -> int:
        return self.length

    def printLListForward(self):
        linked_list = ''
        if self.head is None:
            print("linked list is empty")
        else:
            itr = self.head
            while itr is not None:
                if itr.prevNode is None:
                    linked_list += str(itr.nodeData) + "-->"
                elif itr.nextNode is None:
                    linked_list += "<--" + str(itr.nodeData)
                else:
                    linked_list += "<--" + str(itr.nodeData) + "-->"

                itr = itr.nextNode
            print(linked_list)

    def printLListBackward(self):
        linked_list = ''
        if self.head is None:
            print("linked list is empty")
        else:
            itr = self.getLastItem()
            while itr is not None:
                if itr.prevNode is None:
                    linked_list += "<--" + str(itr.nodeData)

                elif itr.nextNode is None:
                    linked_list += str(itr.nodeData) + "-->"

                else:
                    linked_list += "<--" + str(itr.nodeData) + "-->"
                itr = itr.prevNode
            print(linked_list)


if __name__ == "__main__":
    dblLinkedList = LinkedList()
    dblLinkedList.insertAtBeginning(3)
    dblLinkedList.insertAtEnd(7)
    dblLinkedList.insertValues([1, 9])

    print(dblLinkedList.remove(9))

    print(dblLinkedList.getLength())

    dblLinkedList.printLListForward()
    dblLinkedList.printLListBackward()
