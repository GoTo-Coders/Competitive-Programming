# Link --> https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

# Code:
def decodeHuff(root, s):
    current = root
    answer = ""
    
    for index in s:
        if index == '0' and current.left:
            current = current.left
        elif current.right:
            current = current.right
        
        if current.left is None and current.right is None:
            answer += current.data
            current = root
    
    print(answer)
