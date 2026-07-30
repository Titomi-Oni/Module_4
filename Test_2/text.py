class Book:
    def __init__(self,title,author,is_borrowed):
        self.title = title
    
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if self.is_borrowed == True:
            print ("Is borrowed")

    def return_book(self):
        if self.is_borrowed == False:
            print ("Is not borrowed")