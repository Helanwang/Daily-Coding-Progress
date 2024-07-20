# class Notes

def main():

    class Book:  # This is the Class, Part 1
        def __init__(self, title, author, year_published, genre):
            self.title = title
            self.author = author
            self.year_published = year_published
            self.genre = genre

        def book_info(self):  # This the Method, Part 2
            return (f"This book is called {self.title}, written by {self.author}, published in {self.year_published}, "
                    f"category {self.genre}.")

    #  Individual Objects with parameter in here. Part 3
    book1 = Book("Finding Love", "Helan Wang", "2024", "Romance")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "1960", "Fiction")
    #  Print out the info, Part 4.
    print(book1.book_info())
    print(book2.book_info())


if __name__ == '__main__':
    main()
