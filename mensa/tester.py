import datetime
#2019-10-24

data = 'Donnerstag, 24.10.2019'
splitted = data.split(",")[1].strip()


year = splitted.split(".")[2]
month = splitted.split(".")[1]
day = splitted.split(".")[0]
print(year)
print(month)
print(day)
new_date = year + "-" + month + "-" + day
print(new_date)