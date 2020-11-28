#dates can be tricky to use
#to get the current date and time we use:
from datetime import datetime
current_date = datetime.now()
#the now function returns a datetime object
print('today is ' + str(current_date))

#another example:
today = datetime.now()
print('Today is' + str(today))
from datetime import datetime, timedelta
#timedelta function is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#we can call just formats of dates
print ('Day:' + str(current_date.day))
print('Month: '+ str(current_date.month))

#Converting string data into date
birthday = input('When is you birthday (dd/mm/yyyy)?')
Birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
print ('Birthday: ' + str(Birthday_date))
#to this we can add:
birthday_eve = Birthday_date - one_day
print ('Day before birthday: ' + str(birthday_eve))