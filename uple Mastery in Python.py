# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains 
# information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that 
# lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output 
# should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"



count = 1

def flight_input(flight_info):
    traveler_name = input("Enter traveler name: ").lower().title()
    origin = input("Enter origin: ").lower().title()
    destination = input("Enter destination: ").lower().title()
    flight_info.append((traveler_name, origin, destination))
    
    
    


def itenerary(flight_info):
    global count
    for flight in flight_info:
        traveler_name, origin, destination = flight
        print(f"Itenerary {count}: {traveler_name} - From {origin} to {destination}")
        count += 1

def main():
    flight_info = []
    print("Welcome to Flight Iiteneraries")

    while True:
        add_flight = input("Would you like to add a flight (yes/no): ").lower()

        if add_flight == "yes":
            flight_input(flight_info)

        elif add_flight == "no":
            print("Exit")
            break

        else:
            print("Please enter a valid response.")

    itenerary(flight_info)

main()