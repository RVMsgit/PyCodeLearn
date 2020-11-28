#numbers can be stored in variables
pi = 3.14159
print(pi)
#We can operate with string numbers
first_number = 2
second_number = 4
#Addition
print (first_number + second_number)
#Substraction
print (first_number - second_number)
#Multiplication
print (first_number * second_number)
#Division
print (first_number/second_number)
#Exponent
print (first_number ** second_number)

#Combining strings with numbers can be confusing:
days_in_feb=28 #we have to cenvert the number string with the str
    #str function
print(str(days_in_feb) + ' Days in february')

#Changing a string to a number:
input_number = input ('enter a number')
#to operate strings we convert them using the int or float functions
    #Int gives no decimal numbers
print (int(input_number)*(2))
    #Float function gives Decimal numbers
print (float(input_number)* 2.3)
