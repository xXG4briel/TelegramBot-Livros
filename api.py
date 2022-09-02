from datetime import datetime
# from dateutil.relativedelta import relativedelt

current = datetime.today()
# .strftime("%H:%M")

data = datetime(current.year, current.month, current.day, 15)

# diff = abs(relativedelta(ini, fim))

print(current.strptime(str(current), "%H"), " " , data.second)