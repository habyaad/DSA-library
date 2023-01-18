class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None 

    def addChild(self, childData):
        childData.parent = self
        self.children.append(childData)

    def getLevel(self)->int:
        level = 0
        itr = self
        while itr.parent is not None:
            itr = itr.parent
            level+=1
        return level
    def printTree(self, option):
        space = "  " * self.getLevel()
        if type(option) is str:
            if(option=="name"):
                name_to_print = self.name
            elif(option=="designation"):
                name_to_print = self.designation
            elif(option=="both"):
                name_to_print = f"{self.name} ({self.designation})"
            else:
                raise Exception("enter a valid parameter")
            if self.getLevel()>0:
                print(space + "|__" + name_to_print)
            else:
                print(name_to_print)
            if self.children:
                for child in self.children:
                    child.printTree(option)
        elif type(option) is int:
            if option<0:
                raise Exception("invalid index")
            level = self.getLevel()
            if level<=option:
                name_to_print = f"{self.name} ({self.designation})"
                if self.getLevel()>0:
                    print(space + "|__" + name_to_print)
                else:
                    print(name_to_print)
                if self.children:
                    for child in self.children:
                        child.printTree(option)
        else:
            raise Exception("Enter a valid parameter type")

def buildTree() -> TreeNode:
    ceo = TreeNode("Nilupul","CEO")

    cto = TreeNode("Chinmay", "CTO")
    hr = TreeNode("Gels","HR Head")

    iHead = TreeNode("Vishwa", "Infrastructure Head")
    
    iHead.addChild(TreeNode("Dhaval","Cloud Manager"))
    iHead.addChild(TreeNode("Abhijit","App Manager"))

    cto.addChild(iHead)
    cto.addChild(TreeNode("Aamir", "Application Head"))

    hr.addChild(TreeNode("Peter","Recruitment Manager"))
    hr.addChild(TreeNode("Waqas","Policy Manager"))

    ceo.addChild(cto)
    ceo.addChild(hr)

    return ceo

if __name__ == "__main__":
    root = buildTree()
    
    print("Hierarchy up to index 2:")
    root.printTree(2)

    print("\n")

    print("Hierarchy of name:")
    root.printTree("name")

    print("\n")

    print("Hierarchy of designation:")
    root.printTree("designation")

    print("\n")

    print("Full Hierarchy:")
    root.printTree("both")