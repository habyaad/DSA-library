class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BinaryTreeNode(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(data)
            else:
                self.right.add(data)

    def delete(self, data):
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.right is None and self.left is None:
                self = None
            elif self.right is not None and self.left is None:
                self = self.right
            elif self.left is not None and self.right is None:
                self = self.left
            else:
                min_right_val = self.right.min()
                self.data = min_right_val
                self.right = self.right.delete(min_right_val)
        return self

    def inOrderTraversal(self):
        result = []
        if self.left:
            result += self.left.inOrderTraversal()

        result.append(self.data)

        if self.right:
            result += self.right.inOrderTraversal()
        
        return result
    def preOrderTraversal(self):
        result = []
        result.append(self.data)
        if self.left:
            result += self.left.preOrderTraversal()

        if self.right:
            result += self.right.preOrderTraversal()
        
        return result
    def postOrderTraversal(self):
        result = []

        if self.left:
            result += self.left.postOrderTraversal()

        if self.right:
            result += self.right.postOrderTraversal()
        
        result.append(self.data)

        return result
    
    def exists(self, data)->bool:
        if self.data == data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.exists(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.exists(data)
    def min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.min()
    def max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max()
    def calcSum(self):
        totalSum = 0
        totalSum+=self.data
        if self.left:
            totalSum+=self.left.calcSum()
        if self.right:
            totalSum+=self.right.calcSum()
        return totalSum

if __name__ == "__main__":
    num_list = [15, 12, 27, 20, 7, 14, 88, 23]

    tree_root = BinaryTreeNode(num_list[0])
    for i in range(1, len(num_list)):
        tree_root.add(num_list[i])

    print(tree_root.inOrderTraversal())
    tree_root = tree_root.delete(15)

    print(tree_root.inOrderTraversal())

    print(tree_root.preOrderTraversal())
    print(tree_root.postOrderTraversal())
    print(tree_root.exists(10))
    print(tree_root.min())
    print(tree_root.max())
    print(tree_root.calcSum())