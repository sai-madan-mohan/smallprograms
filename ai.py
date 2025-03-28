from datetime import datetime

def days_between_dates():
    date1 = input("Enter the First date(yyyy-mm-dd): ")
    date2 = input("Enter the second date(yyyy-mm-dd): ")

    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((d2 - d1).days)
        print(f"{difference} days")
    
    except ValueError:
        print("Invalid date format. Please enter date in yyyy-mm-dd format")

days_between_dates()