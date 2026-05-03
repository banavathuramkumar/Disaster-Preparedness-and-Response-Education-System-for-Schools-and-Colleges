from disasters import show_disasters, disaster_info
from location import get_location, location_advice
from simulation import run_simulation

def main():
    while True:
        print("\n=== Disaster Preparedness System ===")
        print("1. View Disaster Information")
        print("2. Location-Based Advice")
        print("3. Run Simulation")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            show_disasters()
            disaster = input("Enter disaster name: ")
            disaster_info(disaster)

        elif choice == "2":
            location = get_location()
            location_advice(location)

        elif choice == "3":
            run_simulation()

        elif choice == "4":
            print("Exiting... Stay Safe!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()