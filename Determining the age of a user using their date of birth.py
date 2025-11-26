import datetime
date = input('pls inter your date of birth: ')

x = datetime.datetime.now()

age = x.year - int(date) 

print(f'your age is {age}')