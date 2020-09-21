from pynotifier import Notification
import psutil
# psutil.sensors_battery() will treturn the informaation
#related to battery
battery = psutil.sensors_battery()
#battery.percent will return the current battery percentage
percent = battery.percent
#Notification(title, description, duration)-- to send notification to desktop
Notification("battery percentage",
            str(percent)+ "%Percent Remaining",
            duration=10).send() 
