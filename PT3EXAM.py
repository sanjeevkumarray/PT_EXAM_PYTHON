print("""SANJEEV KUMAR RAY
ROLL NO -2K18CSUN01082
CLASS -B-TECH CSE 4A""")

#Theoretical Questions:

# Q.1:What is the syntax to call a constructor of a base class from child class
#   ANS: We can call using super()Command.

#Q.2:How is a class made as inherited class (syntax of child class)
  # ANS:
 #class Parent:
  # pass
  #class Child(Parent):
# pass
# Here the class child inherits the class parent

#Q.3: Print an element of a nested dictionary
D = dict(emp1 = {'name': 'Bob', 'job': 'Mgr'},
         emp2 = {'name': 'Kim', 'job': 'Dev'},
         emp3 = {'name': 'Sam', 'job': 'Dev'})

print(D)


#Set B

# Q.1: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
print("Please enter text to print::")
inputchars = input()

if inputchars:
    string = ""
    for i in inputchars:
        if inputchars.index(i) % 2 == 0:
            string += str(i)

    print('-------------------')
    print("You Entered:", inputchars)
    print("Result:")
    print(string)


#Q.2: By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

lists = [12,24,35,24,88,120,155]
lists= [x for x in lists if x!=24]
print (lists)


