# Link --> https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

# Code:
def levelOrder(root):
    if root:
        queue = []
        queue.append(root)
        while queue:
            temp_node = queue[0]
            queue.pop(0)
            
            print(temp_node.info, end = " ")
            
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
