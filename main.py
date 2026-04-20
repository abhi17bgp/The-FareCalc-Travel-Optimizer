from fare.calculator import calculate_fare
from fare.utils import get_float_input, get_time_input, get_vehicle_input
from fare.config import SURGE_START, SURGE_END, SURGE_MULTIPLIER

def main():
    print("Welcome to FareCalc")

    distance = get_float_input()
    vehicle = get_vehicle_input()
    hour, minute = get_time_input()

    try:
        fare = calculate_fare(distance, vehicle, hour)
        surge_applied = SURGE_START <= hour <= SURGE_END
        display_hour = hour % 12 or 12
        period = "AM" if hour < 12 else "PM"
        
        print("\n------ Price Receipt ------")
        print(f"Vehicle Type : {vehicle}")
        print(f"Distance     : {distance} km")
        print(f"Time         : {display_hour}:{minute:02d} {period}")
        if surge_applied:
            print(f"Surge Applied: Yes ({SURGE_MULTIPLIER}x)")
        else:
            print("Surge Applied: No")
        print(f"Total Fare   : ₹{round(fare, 2)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()