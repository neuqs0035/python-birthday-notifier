from plyer import notification
from datetime import date
from time import sleep

while True:

    file = open("birthdays.csv")

    all_birthdays_data = file.readlines()

    str_current_date = str(date.today()).split("-")

    for user in all_birthdays_data:
        
        bdate = user[user.rfind(",") + 1:].removesuffix("\n").split("-")

        if bdate[1] == str_current_date[1]:

            if bdate[0] == str_current_date[2]:

                message = "Today Is " + user[:user.rfind(",")] + " 's Birthday"

                notification.notify(

                    title = "Birthdays",
                    message = message,
                    timeout=15
                    
                )

    
    sleep(7200)