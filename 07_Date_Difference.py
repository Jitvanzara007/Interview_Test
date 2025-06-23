'''Write a Python program that calculates the difference between two dates provided by a user.'''

'''
Subtracting the dates and getting difference (string into dd/mm/yy format)
'''


from datetime import datetime

def calculate_lived_days(start_date, end_date):
    fmt = "%d-%m-%Y"
    d1 = datetime.strptime(start_date, fmt)
    d2 = datetime.strptime(end_date, fmt)
    
    diff=d2-d1
    return diff.days

birth_date = input("Enter your birth date (dd-mm-yyyy): ")
today_date = input("Enter today's date (dd-mm-yyyy): ")

days_lived = calculate_lived_days(birth_date, today_date)
print(f"You have lived {days_lived} days.")
