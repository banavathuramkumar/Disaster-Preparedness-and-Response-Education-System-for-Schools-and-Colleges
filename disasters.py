from utils import load_data, print_steps

data = load_data()

def show_disasters():
    print("\nAvailable Disasters:")
    for disaster in data.keys():
        print("-", disaster)

def disaster_info(disaster_name):
    disaster = data.get(disaster_name.lower())
    
    if disaster:
        print("\nDescription:")
        print(disaster["description"])
        
        print("\nSafety Steps:")
        print_steps(disaster["steps"])
    else:
        print("Disaster not found!")