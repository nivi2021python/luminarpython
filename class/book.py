class Book:
    def setval(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
        print(self.name,self.author,self.pages)
    def __str__(self):
         return self.name + self.author + str(self.pages)

bk=Book()
bk.setval("wings Of Fire","Abdul kalam",698)
print(bk)