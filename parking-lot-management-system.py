class Car: 
    def __init__ (self, license_plate, owner_name):
        self.license_plate = license_plate 
        self.owner_name = owner_name

    def __str__(self):
        return f"License plate {self.license_plate}, Owner {self.owner_name}"

class ParkingLot:

    def __init__ (self, capacity):
        self.parked_cars = {}
        self.capacity = capacity
        self.parking_queue = []

    def park_car(self,car):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[car.license_plate] = car 
            print(f"Car {car.license_plate} has been parked ")
        else:
            self.parking_queue.append(car)
            print(f"Car {car.license_plate} has been taken to the parking queue") 

        
    def remove_car(self, license_plate ):
        if license_plate  in self.parked_cars:
            removed_car = self.parked_cars.pop(license_plate)
            print(f" Car {license_plate} has been removed from the parking lot") 

            if self.parking_queue:
                next_car = self.parking_queue.pop(0)

                self.parked_cars[next_car.license_plate] = next_car
                print(f"Car {next_car.license_plate} from the queue has been parked")
        
        else:
            print(f"{license_plate} not found ")

    def get_available_spots(self):
        # This function returns the empty parking slots 
       available_slots = self.capacity - len(self.parked_cars)
       return f"The number of slots remaining is {available_slots}"
    
    def is_car_parked(self,license_plate):
        if license_plate in self.parked_cars: 
            return f"The car {license_plate} is parked"
        else:
            return f"The car is not parked in the parking lot "
        
    def display_parked_cars(self):
        if not self.parked_cars:
            return "No cars parked in the parking lot"
        else:
            return "\n".join(str(car)for car in self.parked_cars.values())

parking_lot = ParkingLot(2)  # Parking lot with 2 spots

car1 = Car("ABC123", "John Doe")
car2 = Car("XYZ789", "Jane Doe")
car3 = Car("LMN456", "Alice")

parking_lot.park_car(car1)  # Successfully parks
parking_lot.park_car(car2)  # Successfully parks
parking_lot.park_car(car3)  # No space, added to queue

print(parking_lot.get_available_spots())  
# Output: 0

parking_lot.remove_car("ABC123")  # Car leaves, car3 gets parked from queue

print(parking_lot.display_parked_cars())  
# Output: ['XYZ789 - Jane Doe', 'LMN456 - Alice']
