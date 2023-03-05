import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(n, parents):
    nodes = [Node(i) for i in range(n)]

    for i in range(n):
        parent = parents[i]

        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    return root

def get_height(root):
    if not root.children:
        return 1

    max_depth = 0

    for child in root.children:
        max_depth = max(max_depth, get_height(child))

    return max_depth + 1

def compute_height(n, parents):
    root = build_tree(n, parents)
    return get_height(root)

def main():
    
    h = int(input())
    if h == "I":
        n = int(input())   
        parents = list(map(int, input().split()))
        
    else :
        h = int(input())
        
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem.
sys.setrecursionlimit(10**7)

main()
