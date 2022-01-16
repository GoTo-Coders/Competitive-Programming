# Link --> https://www.hackerrank.com/challenges/30-abstract-classes/problem

# Code:class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print("Title: "+title)
        print("Author: "+author)
        print("Price: "+str(price))
