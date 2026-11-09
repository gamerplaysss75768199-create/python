class Book :
    def __init__(self,tittle,author,is_available):
        self.name=tittle
        self.author=author
        self.is_available=is_available

    def issue(self):
        if(self.is_available==True):
            print("book issued")
            self.is_available=False
        else :
            print("book is unavailable")
          
    def return_b(self):
        if(self.is_available==False):
            print("book is returned")
            self.is_available=True
        else: 
            print("book has not been issued") 
    def display(self):
        if (self.is_available==True):
            print(f"name: {self.name} , author: {self.author}")

    def issued(self):
        if(self.is_available==False):
            print(f"{self.name} is issued\n")

b1=Book("C","abc",True)
b2=Book("Python","abc",True)
b3=Book("The subtle art of not giving a fuck","S",True)
b4=Book("utpaat","smriti",True)
b5=Book("utpaat premium edition","smriti",True)
while True :
 choice=int(input("0 to display available books\n1 to issue\n2 to return book\n3 to check Issued books\n4 to exit: "))
 match(choice):
     case 0:
          print("\n")
          b1.display()
          b2.display()
          b3.display()
          b4.display()
          b5.display()
          print("\n")
     case 1 :
         choice=input("which book u want to issue? ")
         match(choice):
             case "C":
                 print("\n")
                 b1.issue()
                 print("\n")
             case "Python":
                 print("\n")
                 b2.issue()
                 print("\n")
             case "The subtle art of not giving a fuck" :
                 print("\n")
                 b3.issue()
                 print("\n")
             case "utpaat":
                 print("\n")
                 b4.issue()
                 print("\n")
             case "utpaat premium edition":
                 print("\n")
                 b5.issue()
                 print("\n")
             case _:
                 print("\n")
                 print("Book is unavailable or is not there")
     case 2 :
           choice=input("which book u want to issue? ")
           match(choice):
               case "C":
                   print("\n")
                   b1.return_b()
                   print("\n")
               case "Python":
                   print("\n")
                   b2.return_b()
                   print("\n")
               case "The subtle art of not giving a fuck" :
                   print("\n")
                   b3.return_b()
                   print("\n")
               case "utpaat":
                 print("\n")
                 b4.return_b()
                 print("\n")
               case "utpaat premium edition":
                 print("\n")
                 b5.return_b()
                 print("\n")
               case _:
                   print("\n")
                   print("Book does not belong to this library")
     case 4:
         print("\n")
         print("**Thanks for coming in our library")
         break
     case 3 :
          print("\n")
          b1.issued()
          b2.issued()
          b3.issued()
          b4.issued()
          b5.issued()
          print("\n")
     case _:
         print("\n")
         print("**INVALID CHOICE**")
         print("\n")
