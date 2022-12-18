# Exercise 1. Rectangle class: 
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

#solution-
class Rectangle:
    # define constructor with attributes: length and width 
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    # Create Perimeter method
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    # Create area method
    def Area(self):
        return self.length*self.width   
    
    # create display method
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())
class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height
        
    # define Volume method
    def volume(self):
        return self.length*self.width*self.height
        
myRectangle = Rectangle(7 , 5)
myRectangle.display()
print("----------------------------------")
myParallelepipede = Parallelepipede(7 , 5 , 2)
print("the volume of myParallelepipede is: " , myParallelepipede.volume())

        






# Exercice 2: Person class and child Student class 
# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.

#solution
class Person:
    # define constructor with name and age as parameters
      def __init__(self, name, age):
        self.name = name
        self.age = age
    # create display method fro Person class
def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
    
# create child class Student of Person class
class Student(Person):
    # define constructor of Student class with section additional parameters 
    def __init__(self, name , age , section):
        Person.__init__(self,name, age)
        self.section = section
    
    # Create display method for Student class
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)
        # Testing Person class
P = Person("Tomas Wild", 37)
P.display()
print("-------------------------------")
S = Student("Albert", 23 , "Mathematics")
S.displayStudent()





# Exercise 3. Bank Account class: 
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
# Give the complete code for the  BankAccount class.
#solution-
class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    # create Deposit() method
    def Deposit(self , d ):
        self.balance = self.balance + d
    
    # create Withdrawal method
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
    # create bankFees() method
    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    # create display() method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        
# Testing the code :
newAccount = BankAccount(2178514584, "Albert" , 2700)
# Creating Withdrawal Test
newAccount.Withdrawal(300)
# Create deposit test
newAccount.Deposit(200)
# Display account informations
newAccount.display()






# Exercise 4. Circle class 
# 1 - Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
#    def __init__(self,a,b,r):         
#         self.a = a         
#         self.b = b         
#         self.r = r

# 2 - Define a Area() method of the class which calculates the area of ​​the circle.
# 3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
# 4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
#solution-
from math import pi
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter (self):
        return  2 * pi * self.r


    def area (self):
        return  pi * self.r**2
    

    # form of the cercle equation 
    def formEquation (self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    
    # method to test if given point blong to the circle or not 
    def test_belong (self, x, y):
        if (self.formEquation (x, y) == 0):
            print ("the point: (", x, y, ") belongs to the circle C")
        else:
            print ("the point: (", x, y, ") does not belong to the circle C")


# Creating of an instance object
C = Circle (1,2,1)

print ("the perimeter of the circle C is:", C.perimeter() )
print ("the area of circle C is:", C.area())
# we test if the point(1,1) belong to the circle or not
C.test_belong(1,1) 
# The output is:
#the perimeter of the circle C is: 6.283185307179586
#the area of circle C is: 3.141592653589793
#the point: ( 1 1 ) belongs to the circle C







# Exercise 5. Computation class
# 1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
#solution-
class Computation:
    def __init__ (self):
        pass
# --- Factorial ------------
    def factorial(self, n):
        j = 1
        for i in range (1, n + 1):
            j = j * i
        return j
    
# --- Sum of the first n numbers ----
    def sum (self, n):
        j = 1
        for i in range (1, n + 1):
            j = j + i
        return j
    
# --- Primality test of a number ------------
    def testPrim (self, n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
             return True
        else:
            return False

# --- Primality test of two integers ------------
    def testprims (self, n, m):
        
        # initialize the number of commons divisors
        commonDiv = 0
        for i in range (1, n + 1):
            if (n% i == 0 and m% i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print ("The numbers", n, "and", m, "are co-primes")
        else:
            print ("The numbers", n, "and", m, "are not co-primes")

#---Multiplication table-------------
    def tableMult (self, k):
        for i in range (1,10):
            print (i, "x", k, "=", i * k)

# --- All multiplication tables of the numbers 1, 2, .., 9
    def allTables (self):
        for k in range (1,10):
            print ("\nthe multiplication table of:", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)

# ----- list of divisors of an integer
    def listDiv (self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0):
                lDiv.append (i)
        return lDiv

# ------ list of prime divisors of an integer ----------------
    def listDivPrim (self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0 and self.testPrim (i)):
                lDiv.append (i)
        return lDiv
        # Instantiation example
Comput= Computation ()
Comput.testprims (13, 7)
print ("List of divisors of 18:", Comput.listDiv (18))
print ("List of prime divisors of 18:", Comput.listDivPrim (18))
Comput.allTables ()


 
 
# Exercise 6 Class Book 
#  Define a Book class with the following attributes: Title, Author (Full name), Price.
# Define a constructor used to initialize the attributes of the method with values entered by the user.
# Set the View() method to display information for the current book.
# Write a program to testing the Book class.
#solution-
class Book:
     
     def __init__(self , Title , Author , Price):
          self.Title    =  Title
          self.Author   =  Author
          self.Price    =  Price
          
     
     def view(self ):
          return ("Book Title: " , self.Title ,  "Book Author: " , self.Author, "Book Price: " , self.Price)
          

MyBook = Book("Python Crash Course" , "Eric Matthes" , "23 $")          
print( MyBook.view())





# Exercise 7 Class Tkinter Extended
# 1- Create a class called TK_extended which inherits from TK class and having the attributes:
# - Master: that represents the name of the main window
# - title: that represents the title of the main window
# 2 - Create a method called create() that creates the window
# 3 - Create a method called resize(width, height) that can resize the window.
# 4 - Create a method called generate() to generate the window

#solution-
from tkinter import*
# Question 1
class TK_extended(Tk):

    def __init__(self, master , title):
        self.master = master
        self.title = title
    #------------    
    # Question 2 
    #------------
    def create(self):
        self.master = Tk()
        self.master.title(self.title)        
    
    #------------    
    # Question 3 
    #------------        
    def resize(self, width , height):
        self.master.geometry("{}x{}".format(width , height))
        def generate(self):
           self.master.mainloop() 
        
        
#------------    
# Execution 
#------------        
root = TK_extended("win" , "My Window")
root.create()
root.resize(500 , 300)
root.generate()
       