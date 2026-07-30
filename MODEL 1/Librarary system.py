class Books:
    def __init__ (self,title,author):
        self.title = title
        self.author = author
    is_borrowed = True

    if is_borrowed == False:
        print("The book is borrwed")
    else:
        print("The book is returned")
