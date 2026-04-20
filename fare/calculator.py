from .config import RATES, SURGE_START, SURGE_END, SURGE_MULTIPLIER


def calculate_fare(distance, vehicle_type, hour):
    rate = RATES[vehicle_type]
    base_fare = distance * rate

    if SURGE_START <= hour <= SURGE_END:
        return base_fare * SURGE_MULTIPLIER

    return base_fare