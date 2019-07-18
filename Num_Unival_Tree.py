##This Program is to count the number of Uni-value subtrees in a binary tree
##Throught Process
##1. leaf node is always a uni-value subtree(first count number of leaf node)
##2. Count the subtree that at least 2 depth:
  ##firstly check the ones with 2 depth, if it's a uni-value subtree,
  ##increase count, also remove all the left/right node of the uni-value 2 depth tree
  ##(which is updating the 2 depth uni-value tree to be a leaf node as I go)
  ##that way we can reuse the function to check the 2 depth uni-value subtree again to check the 3 depth/4 depth
  ##in the while loop!
  ##we will break out the while loop
  ##if the "2 depth uni-value subtree count" stays the same compare to the last time running the function!

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def numLeaf(self):
        if self.root:
            leafCount = 0
            leafCount = self.numLeafNode(self.root, leafCount)
        return leafCount

    def numLeafNode(self, nodeToCount, leafCount):
        if (not nodeToCount.left) and (not nodeToCount.right):
            leafCount += 1
        else:
            if nodeToCount.left:
                leafCount = self.numLeafNode(nodeToCount.left, leafCount)
            if nodeToCount.right:
                leafCount = self.numLeafNode(nodeToCount.right, leafCount)

        return leafCount

    def numDepth2(self):
        if self.root:
            PreviousCount = -1
            Depth2Count = 0
            tempNode = self.root
            while (Depth2Count - PreviousCount != 0):
                PreviousCount = Depth2Count
                (Depth2Count, tempNode) = self.numDepth2Node(tempNode, Depth2Count, tempNode)
        return Depth2Count

    ##I'm updating the 2 depth uni-value tree to be a leaf node as I go
    ##so this function counts all the uni-value subtrees
    ##that 2 or more depth
    def numDepth2Node(self, nodeToCount, subTreeCount, origNode):
        leftNode = nodeToCount.left
        rightNode = nodeToCount.right

        if (not leftNode) and (not rightNode):
            pass
        elif (not leftNode) and (not rightNode.left) and (not rightNode.right):
            if rightNode.value == nodeToCount.value:
                subTreeCount += 1
                nodeToCount.right = None
        elif (not rightNode) and (not leftNode.left) and (not leftNode.right):
            if leftNode.value == nodeToCount.value:
                subTreeCount += 1
                nodeToCount.left = None
        elif (not rightNode.left) and (not rightNode.right) and (not leftNode.left) and (not leftNode.right):
            if leftNode.value == nodeToCount.value and nodeToCount.value == rightNode.value:
                subTreeCount += 1
                nodeToCount.left = None
                nodeToCount.right = None
        else:
            if leftNode:
                (subTreeCount, origNode) = self.numDepth2Node(leftNode, subTreeCount, nodeToCount)
            if rightNode:
                (subTreeCount, origNode) = self.numDepth2Node(rightNode, subTreeCount, nodeToCount)

        return (subTreeCount, origNode)

    def numUnivTree(self):
        ##first traverse the tree to count the number of leaf nodes
        ##all the leaf nodes are univtree
        numLeaf = self.numLeaf()

        ##second count the subtrees that have depth of at least 2
        if numLeaf <= 2:
            return numLeaf
        else:
            numDepth2 = self.numDepth2()
            return(numLeaf + numDepth2)

#######Tests
#######make a tree
N1 = Node(0)
N2 = Node(1)
N3 = Node(0)
N4 = Node(1)
N5 = Node(0)
N6 = Node(1)
N7 = Node(1)

N1.left = N2
N1.right = N3
N3.left = N4
N3.right = N5
N4.left = N6
N4.right = N7

Tree1 = Tree()
Tree1.root = N1

print(Tree1.numUnivTree())


NN1 = Node(5)
NN2 = Node(1)
NN3 = Node(5)
NN4 = Node(5)
NN5 = Node(5)
NN6 = Node(5)


NN1.left = NN2
NN1.right = NN3
NN2.left = NN4
NN2.right = NN5
NN3.right = NN6


Tree2 = Tree()
Tree2.root = NN1

print(Tree2.numUnivTree())
