from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def buildTree(ip):
    root = TreeNode(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size + 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]

        #Если левый ребенок не 0
        if currVal != "N":
            # Создаем левого ребенка
            currNode.left = TreeNode(int(currVal))
            q.append(currNode.left)
            size = size + 1

        i = i + 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != "N":
            # Создаем левого ребенка
            currNode.right = TreeNode(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
        
    return root



def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level+1)
        print(3 * ' ' * level + str(node.val))
        print_tree(node.left, level=level + 1)


class Solution:
    # def bstToGst(self, root: TreeNode) -> TreeNode:
    #
    #     self.inorder = []
    #
    #     def _inorder_traversal(node):
    #         if node is not None:
    #             _inorder_traversal(node.left)
    #             self.inorder.append(node)
    #             _inorder_traversal(node.right)
    #
    #     _inorder_traversal(root)
    #
    #
    #     n = len(self.inorder)
    #     cur = self.inorder[-1].val
    #     cumsum = [cur]
    #     for i in range (n-2, -1, -1):
    #         cur = cur + self.inorder[i].val
    #         cumsum.append(cur)
    #
    #
    #     for i, node in enumerate(self.inorder):
    #         node.val = cumsum[n-1-i]
    #
    #
    #
    #     return root
    val = 0
    def bstToGst(self, root: TreeNode):
        if root.right: self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.bstToGst(root.left)

        return root



if __name__ == '__main__':
    root_arr = [4, 1, 6, 0, 2, 5, 7, 'N', 'N', 'N', 3, 'N', 'N', 'N', 8]
    root = buildTree(root_arr)
    print_tree(root)
    print(Solution().bstToGst(root))
    print_tree(root)