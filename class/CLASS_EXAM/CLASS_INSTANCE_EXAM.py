class Book:
    def __init__(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def prnt_bookdetail(self):
        print(self.library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)

bk=Book("holy angels","wings of fire","A P J Abdul Kalam",678)
bk.prnt_bookdetail()