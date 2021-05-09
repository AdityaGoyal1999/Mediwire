from django.apps import AppConfig

from trycourier import Courier

client = Courier(auth_token="dk_prod_A7WSYECSE1MD0XNJA0NX6R6CF8ME")

email = 'arjunmishra31204@gmail.com'
phone_number = '+91930-540-4004'
name = "Arjun Mishra"
date = "May 10"
time = "11:00 AM"
phone = "+14155390336"

resp = client.send(
  event="3Y5ZJNY5B0MGBBH87DB1SY3T9C0P",
  recipient="e12fef96-8731-4c35-b3ae-6cb81f373652",
  profile={
    email: "arjunmishra31204@gmail.com",
    phone_number: "+91930-540-4004",
  },
  data={
    name: "Arjun",
    date: "May 10",
    time: "11:00 AM",
    phone: "+14155390336",
  },
)
print(resp['messageId'])

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
