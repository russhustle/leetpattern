from enum import Enum, auto


class VehicleSize(Enum):
    MOTORCYCLE = auto()
    COMPACT = auto()
    LARGE = auto()


class Vehicle:
    def __init__(self, license_plate: str, size: VehicleSize):
        self.license_plate = license_plate
        self.size = size


class ParkingSpot:
    def __init__(self, size: VehicleSize):
        self.size = size
        self.vehicle = None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.vehicle is not None:
            return False
        return self.size.value >= vehicle.size.value

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None


class ParkingLot:
    def __init__(self):
        self.spots = {
            VehicleSize.MOTORCYCLE: [],
            VehicleSize.COMPACT: [],
            VehicleSize.LARGE: [],
        }

    def add_parking_spot(self, spot: ParkingSpot):
        self.spots[spot.size].append(spot)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.spots[vehicle.size]:
            if spot.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle: Vehicle):
        for spot_list in self.spots.values():
            for spot in spot_list:
                if spot.vehicle == vehicle:
                    spot.remove_vehicle()
                    return True
        return False


if __name__ == "__main__":
    parking_lot = ParkingLot()
    parking_lot.add_parking_spot(ParkingSpot(VehicleSize.MOTORCYCLE))
    parking_lot.add_parking_spot(ParkingSpot(VehicleSize.COMPACT))
    parking_lot.add_parking_spot(ParkingSpot(VehicleSize.LARGE))
    vehicle1 = Vehicle("ABC123", VehicleSize.MOTORCYCLE)
    vehicle2 = Vehicle("XYZ456", VehicleSize.COMPACT)
    vehicle3 = Vehicle("DEF789", VehicleSize.LARGE)
    print(parking_lot.park_vehicle(vehicle1))  # True
    print(parking_lot.park_vehicle(vehicle2))  # True
    print(parking_lot.park_vehicle(vehicle3))  # True
    print(parking_lot.park_vehicle(Vehicle("GHI101", VehicleSize.LARGE)))  # False
