class Node:
    def __init__(self, nData, nextN):
        self.nodeData = nData
        self.nextNode = nextN


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion processes
    def insertAtBeginning(self, newData):
        node = Node(newData, self.head)
        self.head = node

    def insertAtEnd(self, newData):
        node = Node(newData, None)
        if self.head is None:
            self.head = node
        else:
            itr = self.head
            while itr is not None:
                if itr.nextNode is None:
                    itr.nextNode = node
                    break
                itr = itr.nextNode

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
                    node = Node(newData, itr.nextNode)
                    itr.nextNode = node
                    break

                count += 1
                itr = itr.nextNode

    # removal processes
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.nextNode
        else:
            itr = self.head
            count = 0
            while itr is not None:
                if count == index-1:
                    itr.nextNode = itr.nextNode.nextNode
                    break
                itr = itr.nextNode
                count += 1

    def remove(self, value):
        if self.exists(value):
            itr = self.head
            if itr.nodeData == value:
                self.head = self.head.nextNode
            else:
                while itr is not None:

                    if itr.nextNode.nodeData == value:
                        itr.nextNode = itr.nextNode.nextNode
                        break
                    itr = itr.nextNode
        else:
            raise Exception(f"{value} does not exist in the linked list")

    def exists(self, value) ->  bool:
        
        return True if self.count(value)>0 else False

    def index(self, value) ->  int:
            itr = self.head
            count = 0
            if self.exists(value):
                while itr is not None:
                    if itr.nodeData == value:
                        return count
                    itr = itr.nextNode
                    count+=1
            else:
                raise Exception(f"{value} does not exist in linked list")
    # return length of items in linked list
    def getLength(self) -> int:
        itr = self.head
        count = 0
        while itr is not None:
            count += 1
            itr = itr.nextNode
        return count

    def count(self, value) -> int:
        itr = self.head
        count = 0
        while itr is not None:
            if itr.nodeData == value:
                count += 1
            itr = itr.nextNode
        return count
    # print linked list

    def printLList(self):
        linked_list = ''
        if self.head is None:
            print("linked list is empty")
        else:
            itr = self.head
            while itr is not None:
                if itr.nextNode is None:
                    linked_list += str(itr.nodeData)
                else:
                    linked_list += str(itr.nodeData) + "-->"

                itr = itr.nextNode
            print(linked_list)


if __name__ == "__main__":
    linkedList = LinkedList()

    linkedList.insertAtEnd(8)
    linkedList.insertAtEnd(80)
    linkedList.insertAtEnd(800)
    
    linkedList.insertValues([1, 2, 3, 4])
    linkedList.insertAt(4, 100)
    print(linkedList.index(4))
    print(linkedList.removeAt(8000))

    linkedList.printLList()
