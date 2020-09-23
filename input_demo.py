
#getting string as an input
name= input('Enter a name: ')
print("Hello {}".format(name.title()))

#getting integer/float as an input
num= int(input('Enter a number: '))
print("Entered number is {}".format(num))

num= float(input('Enter a number: '))
print("Entered floating number is {}".format(num))


#eval. This function evaluates a string as a line of Python.
#If the user inputs 2 * 3, this outputs 6.
result = eval(input("Enter an expression: "))
print(result)