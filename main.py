from fare.calculator import calculate_fare
from fare.utils import get_float_input, get_time_input, get_vehicle_input


def main():
    print("Welcome to FareCalc")

    distance = get_float_input()
    vehicle = get_vehicle_input()
    hour, minute = get_time_input()

    try:
        fare = calculate_fare(distance, vehicle, hour)
        display_hour = hour % 12 or 12
        period = "AM" if hour < 12 else "PM"
        
        print("\n------ Price Receipt ------")
        print(f"Vehicle Type : {vehicle}")
        print(f"Distance     : {distance} km")
        print(f"Time         : {display_hour}:{minute:02d} {period}")
        print(f"Total Fare   : ₹{round(fare, 2)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()