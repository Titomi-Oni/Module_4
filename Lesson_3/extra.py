class Book:
        def ___init__(self, title, author):
            self.title = title
            self.author = author

        def display_info():
            print ("Title: ",self.title)
            print ("Author: ",self.author)

class EBook(Book):
        def __init__(self, file_format, file_size):
              self.file_format = file_format
              self.file_size = file_size
              super()(self, file_format, file_size)

              
Override the display_info() method in EBook so that it displays:

File Format

File Size

Then calls the parent class method to display the book details.

Part 5: Add a New Method

Create a method named download() that prints:

Downloading the eBook...

Part 6: Create an Object