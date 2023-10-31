import heapq


# Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None) -> None:
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        # Huffman Tree directions(0 for left, 1 for right)
        self.huff = ""

    def __lt__(self, next):
        return self.freq < next.freq


# Print Node
def printNodes(node, val=""):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


# Main
if __name__ == "__main__":
    # Input Data
    chrs = ["a", "b", "c", "d", "e", "f"]
    freq = [5, 9, 12, 13, 16, 45]
    nodes = []

    # Build Huffman Tree
    for i in range(len(chrs)):
        heapq.heappush(nodes, node(freq[i], chrs[i]))

    # Build Huffman Code
    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)
        node2 = heapq.heappop(nodes)
        node1.huff = 0
        node2.huff = 1
        newNode = node(
            node1.freq + node2.freq, node1.symbol + node2.symbol, node1, node2
        )
        heapq.heappush(nodes, newNode)

    # Print Huffman Code
    printNodes(nodes[0])
