import heapq

class node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq    # frequency of char

        self.char = char    # char name (character)

        self.left = left    # node left of current node

        self.right = right    # node right of current node

        self.huff = ''    # tree direction (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''): #node nor nodes
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # if node is edge node then
    # display its huffman code
    if (not node.left and not node.right):
        print(f"{node.char} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45] # frequency of characters

nodes = [] # list containing unused nodes

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x])) #first nodes and then node

while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1 #IMP

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq + right.freq, left.char + right.char, left, right)

    heapq.heappush(nodes, newNode)

printNodes(nodes[0])


