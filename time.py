time = int(input("Please enter the number of seconds you want to convert to minutes or hours: "))

##if time.isdigit():
##    print(time)
##else:
##    print("No match")
##    #break

# months have 60 sec * 60 min * 24 hrs * 30 days = 2,592,000 sec
months = time // 2592000
# days have 60 sec * 60 min * 24 hrs = 86400 sec
days = (time % 2592000) // 30
# hours have 60 sec * 60 min = 3600 sec
hours = (time % 86400) // 24
# minutes have 60 sec
minutes = (time % 3600) // 60
seconds =  time - ((days * 86400) + (hours * 3600) + (minutes * 60))

months = days // 30
years = days // 365
print(time, "seconds is: ")
print(years, "year(s) (assuming a 365 day year)")
print(months, "month(s) (assuming a 30 day month)")
print(days, "day(s)")
print(hours, "hour(s)")
print(minutes, "minute(s)")
print(seconds, "second(s)")
