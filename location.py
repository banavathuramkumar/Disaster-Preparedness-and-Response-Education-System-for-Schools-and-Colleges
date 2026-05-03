def get_location():
    print("\nSelect your region:")
    print("1. Coastal Area")
    print("2. Urban Area")
    print("3. Rural Area")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        return "Coastal"
    elif choice == "2":
        return "Urban"
    elif choice == "3":
        return "Rural"
    else:
        return "Unknown"

def location_advice(location):
    print(f"\nSafety Advice for {location} Area:")

    if location == "Coastal":
        print("- Be aware of floods and cyclones")
    elif location == "Urban":
        print("- Be cautious about fire and earthquakes")
    elif location == "Rural":
        print("- Prepare for floods and lack of emergency services")
    else:
        print("- General safety awareness is important")