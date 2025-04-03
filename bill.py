def split_bill():
    try:
        total_bill = float(input("Enter total bill amount: ₹"))
        people = int(input("Enter the number of people: "))

        if people <= 0:
            print(" Number of people must be at least 1!")
            return

        per_person = total_bill / people
        print(f"\nEach person should pay: ₹{per_person:.2f}")

    except ValueError:
        print("Please enter valid numbers!")

split_bill()
