class Node:
    
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
       

def getLCA(root, x1, x2):

    if root is None:
        return None

    if root.key == x1 or root.key == x2:
        return root

    right = getLCA(root.right, x1, x2)
    left = getLCA(root.left, x1, x2)
   

    if left and right:
        return root

    return left if left is not None else right

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)