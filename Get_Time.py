#Get world date and time using python
# importing datetime
from datetime import datetime
# pip install pytz
#pytz = python timezone module
import pytz
#getting timezone of america/new york 
country_time_zone = pytz.timezone('America/new_york')
# getting date and time of america/new_york
country_time = datetime.now(country_time_zone)
# printing dte and time of america/new_york
print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))


