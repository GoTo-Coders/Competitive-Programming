# Link --> https://www.hackerrank.com/challenges/30-binary-trees/problem

# Code:
def levelOrder(self,root):
        queue = []
        queue.append(root)
        
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.data, end=" ")
