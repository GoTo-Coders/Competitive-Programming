# Link --> https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

# Code:
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if current.info > val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break    
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
