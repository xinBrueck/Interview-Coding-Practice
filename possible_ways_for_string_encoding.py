##Given the mapping a = 1, b = 2, ... z = 26, and an encoded message as a string,
##count the number of ways it can be decoded.
##we can assume the encoded message is decodable

##for example 111 can be decoded as aaa, ak, ka

##I have implemented this using a tree structure
##starting at index 0 for the message
##if I can decode the next 1 digit, I will build a left node, index += 1
##if I can decode the next 2 digit together, I will build a right node, index += 2
##then recursively build the tree

##after I build the tree structure
##I can count the number of leaf node, and that's the number of possible solutions!

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildPossibleTree(valueString, startingIndex, treeNode):
    if startingIndex <= len(valueString)-2:
        if int(valueString[startingIndex+1]) == 0:
            treeNode.right = Node(2)
            buildPossibleTree(valueString, startingIndex+2, treeNode.right)
        elif (startingIndex+2 < len(valueString)) and int(valueString[startingIndex+2]) == 0:
            treeNode.left = Node(1)
            buildPossibleTree(valueString, startingIndex+1, treeNode.left)
        elif int(valueString[startingIndex]) == 1 or (int(valueString[startingIndex]) == 2 and int(valueString[startingIndex+1]) in range(1, 7)):
            treeNode.left = Node(1)
            buildPossibleTree(valueString, startingIndex+1, treeNode.left)
            treeNode.right = Node(2)
            buildPossibleTree(valueString, startingIndex+2, treeNode.right)
        elif int(valueString[startingIndex]) in range(3, 10) or int(valueString[startingIndex+1]) in range(7, 10):
            treeNode.left = Node(1)
            buildPossibleTree(valueString, startingIndex+1, treeNode.left)
    elif startingIndex == len(valueString)-1:
        treeNode.left = Node(1)
        return
    else: return
    return treeNode


def countLeafNode(treeNode, leafCount):
    if (not treeNode.left) and (not treeNode.right):
        leafCount += 1
    else:
        if treeNode.left:
            leafCount = countLeafNode(treeNode.left, leafCount)

        if treeNode.right:
            leafCount = countLeafNode(treeNode.right, leafCount)

    return leafCount

def Traverse(nodeToTraverse):  ##to check whether the tree is building right
    print(nodeToTraverse.value, " ")
    if nodeToTraverse.left:
        Traverse(nodeToTraverse.left)

    if nodeToTraverse.right:
        Traverse(nodeToTraverse.right)


##tests
string1 = "111"
treeNodeStart1 = Node(0)
tree1 = buildPossibleTree(string1, 0, treeNodeStart1)
#Traverse(tree1)
possibleSolutionCount1 = countLeafNode(tree1, 0)
print("possible number of solution for {} is {}".format(string1, possibleSolutionCount1))



string2 = "12014"
treeNodeStart2 = Node(0)
tree2 = buildPossibleTree(string2, 0, treeNodeStart2)
#Traverse(tree2)
possibleSolutionCount2 = countLeafNode(tree2, 0)
print("possible number of solution for {} is {}".format(string2, possibleSolutionCount2))



string3 = "1201426"
treeNodeStart3 = Node(0)
tree3 = buildPossibleTree(string3, 0, treeNodeStart3)
#Traverse(tree3)
possibleSolutionCount3 = countLeafNode(tree3, 0)
print("possible number of solution for {} is {}".format(string3, possibleSolutionCount3))
