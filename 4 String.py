#Strings can be stored inside variables
#Strings are text elements in a way
first_name = 'christopher'
print (first_name)

#Combining strings with the plus sign
Last_name = 'Harrison'
print(first_name + Last_name)
print('hello' + first_name + ' ' + Last_name)

#Modifying strings: upper, lower capitalize, count
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

#Example
first_name = input('What is your first name?')
Last_name = input('What is your last name?')
print('Hello' + ' ' + first_name.capitalize() + ' ' + Last_name.capitalize())
