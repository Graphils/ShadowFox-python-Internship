city = input("Enter a city name:")
if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(city + " is in Australia")

elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(city + " is in UAE")

elif city in ["Mumbai", "Bangalore", "Chennai", "delhi"]:
    print(city + " is in India")

else:
    print("City not found in the system.")