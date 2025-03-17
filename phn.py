import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get country
        country = geocoder.description_for_number(parsed_number, "en")

        # Get carrier
        sim_carrier = carrier.name_for_number(parsed_number, "en")

        # Get timezone
        time_zones = timezone.time_zones_for_number(parsed_number)

        print(f"\n📞 Phone Number: {phone_number}")
        print(f"🌍 Country: {country}")
        print(f"📡 Carrier: {sim_carrier}")
        print(f"⏳ Time Zone: {', '.join(time_zones)}")

    except Exception as e:
        print("❌ Invalid phone number! Please check and try again.")

# User input
phone_number = input("Enter phone number (with country code, e.g., +1xxxxxxxxxx): ")
get_phone_number_info(phone_number)
