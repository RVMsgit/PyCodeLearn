#This formats are used to make adding stringd easier
#Example:
first_name = input ('Writte your first name')
last_name = input ('Writte last name')
#Tedious method would be:
print ('Hello' + ' ' + first_name.capitalize() + ' ' + last_name.capitalize())
#But a better method are formats:

# 1st format:
output1 = 'Hello, ' + first_name + ' ' + last_name
print(output1)
#2nd method: 
output2 = 'Hello, {} {}'.format(first_name, last_name)
print(output2)
#3rd method:
output3 = 'Hello, {0} {1}'.format(first_name, last_name)
print(output3)
#4rth method (only in python 3)
output4 = f'Hello, {first_name} {last_name}'
