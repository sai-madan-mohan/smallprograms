from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    # Calculate years, months, and days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust if birth month/day hasn't occurred yet this year
    if days < 0:
        months -= 1
        days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month - 1, 1)).days  

    if months < 0:
        years -= 1
        months += 12  

    print(f"\n🎂 Your Exact Age: {years} years, {months} months, and {days} days.")

# User input
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
calculate_age(birthdate)
