
class Book:
    def __init__(self, title="", author=""):

        """
        Constructor of Book class

        :param author: The author of the book
        :param title:  The title of the book
         """
        self.author = author
        self.title = title

    
    def display(self):

        print(f" {self.title}, written by {self.author}. ")


if __name__ == "__main__":

    b1 = Book("Harry Potter and the Goblet of Fire", "J. K. Rowling")
    b2 = Book("Ivanhoe: A Romance", "Walter Scott")


    b1.display()
    b2.display()
