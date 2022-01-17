# Link --> https://www.hackerrank.com/challenges/equal-stacks/problem

# Code:
def equalStacks(h1, h2, h3):
    stack1 = []
    stack2 = []
    stack3 = []
    
    currentHeight = 0
    for i in h1[::-1]:
        currentHeight += i
        stack1.append(currentHeight)
        
    currentHeight = 0
    for i in h2[::-1]:
        currentHeight += i
        stack2.append(currentHeight)
        
    currentHeight = 0
    for i in h3[::-1]:
        currentHeight += i
        stack3.append(currentHeight)
    
    while True:
        if not stack1 or not stack2 or not stack3:
            return 0    
        
        top1 = stack1[len(stack1) - 1]
        top2 = stack2[len(stack2) - 1]
        top3 = stack3[len(stack3) - 1]
    
        if top1 == top2 and top2 == top3:
            return top1
    
        if top1 >= top2 and top1 >= top3:
            stack1.pop()
        elif top2 >= top1 and top2 >= top3:
            stack2.pop()
        else:
            stack3.pop()
