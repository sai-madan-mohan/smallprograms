def weight_converter(kg):
    print(f"\n🔁 {kg} kilograms is:")
    print(f"{kg * 2.20462:.2f} pounds")
    print(f"{kg * 1000:.2f} grams")

def distance_converter(km):
    print(f"\n🔁 {km} kilometers is:")
    print(f"{km * 0.621371:.2f} miles")
    print(f"{km * 1000:.2f} meters")

def temperature_converter(celsius):
    print(f"\n🌡️ {celsius}°C is:")
    print(f"{(celsius * 9/5) + 32:.2f}°F")
    print(f"{celsius + 273.15:.2f}K")

def unit_comparison_tool():
    print("📐 Welcome to Unit Comparison Tool!")
    print("Choose a category to convert:")
    print("1. Weight (kg to lbs, grams)")
    print("2. Distance (km to miles, meters)")
    print("3. Temperature (Celsius to Fahrenheit, Kelvin)")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        weight_converter(kg)
    elif choice == "2":
        km = float(input("Enter distance in kilometers: "))
        distance_converter(km)
    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        temperature_converter(c)
    else:
        print("❌ Invalid choice. Please try again.")

unit_comparison_tool()
