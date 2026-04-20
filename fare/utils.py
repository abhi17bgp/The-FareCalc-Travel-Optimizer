from fare.config import RATES


def get_float_input():
    while True:
        value = input("Enter distance (km): ").strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number (e.g., 10 or 10.5).")


def get_time_input():
    while True:
        time_input = input("Enter time (HH:MM AM/PM): ").strip().upper()

        try:
            parts = time_input.split()

            if len(parts) != 2:
                print("Invalid format! Use HH:MM AM/PM")
                continue

            time_part = parts[0]
            period = parts[1]

            time_parts = time_part.split(":")

            if len(time_parts) != 2:
                print("Invalid format! Use HH:MM")
                continue

            hour = int(time_parts[0])
            minute = int(time_parts[1])

            if hour < 1 or hour > 12:
                print("Hour must be between 1 and 12.")
                continue

            if minute < 0 or minute > 59:
                print("Minutes must be between 0 and 59.")
                continue

            if period not in ["AM", "PM"]:
                print("Please enter AM or PM.")
                continue

            if period == "AM":
                if hour == 12:
                    hour = 0
            else:  # PM
                if hour != 12:
                    hour += 12

            return hour, minute

        except:
            print("Invalid input! Example: 11:23 PM")


def get_vehicle_input():
    while True:
        vehicle = input("Enter vehicle type (Economy/Premium/SUV): ").strip().upper()

        if vehicle in RATES:
            return vehicle
        else:
            print("Service Not Available for this Vehicle")