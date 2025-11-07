# Base Vehicle Class
class Vehicle:
    def __init__(self, brand, model, year, max_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self._engine_status = "off"  # Encapsulated attribute
    
    def start_engine(self):
        self._engine_status = "on"
        return f"🚀 {self.brand} {self.model} engine started!"
    
    def stop_engine(self):
        self._engine_status = "off"
        return f"🛑 {self.brand} {self.model} engine stopped!"
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model} (Max Speed: {self.max_speed} km/h)"
    
    # Getter for encapsulated attribute
    def get_engine_status(self):
        return self._engine_status


# Car Class (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, year, max_speed, fuel_type, doors):
        super().__init__(brand, model, year, max_speed)
        self.fuel_type = fuel_type
        self.doors = doors
        self._current_gear = "P"  # Encapsulated
    
    def move(self):
        if self.get_engine_status() == "off":
            return "❌ Start the engine first!"
        return f"🚗 Driving {self.brand} {self.model} on the road at up to {self.max_speed} km/h"
    
    def change_gear(self, gear):
        gears = ["P", "R", "N", "D"]
        if gear in gears:
            self._current_gear = gear
            return f"⚙️ Gear changed to {gear}"
        return "❌ Invalid gear!"
    
    def get_info(self):  # Polymorphism
        return f"🚗 {super().get_info()} | Fuel: {self.fuel_type} | Doors: {self.doors}"


# Airplane Class (Inherits from Vehicle)
class Airplane(Vehicle):
    def __init__(self, brand, model, year, max_speed, wingspan, capacity):
        super().__init__(brand, model, year, max_speed)
        self.wingspan = wingspan
        self.capacity = capacity
        self._altitude = 0  # Encapsulated
    
    def move(self):
        if self.get_engine_status() == "off":
            return "❌ Start the engines first!"
        return f"✈️ Flying {self.brand} {self.model} in the sky at up to {self.max_speed} km/h"
    
    def take_off(self):
        if self.get_engine_status() == "on":
            self._altitude = 10000
            return "🛫 Airplane taking off! Climbing to 10,000 feet"
        return "❌ Start engines before takeoff!"
    
    def get_altitude(self):
        return f"📊 Current altitude: {self._altitude} feet"
    
    def get_info(self):  # Polymorphism
        return f"✈️ {super().get_info()} | Wingspan: {self.wingspan}m | Capacity: {self.capacity} passengers"


# Boat Class (Inherits from Vehicle)
class Boat(Vehicle):
    def __init__(self, brand, model, year, max_speed, boat_type, length):
        super().__init__(brand, model, year, max_speed)
        self.boat_type = boat_type
        self.length = length
        self._anchor_dropped = False
    
    def move(self):
        if self.get_engine_status() == "off":
            return "❌ Start the engine first!"
        if self._anchor_dropped:
            return "⛵ Raise the anchor first!"
        return f"🚢 Sailing {self.brand} {self.model} on water at up to {self.max_speed} knots"
    
    def drop_anchor(self):
        self._anchor_dropped = True
        return "⚓ Anchor dropped! Boat is stationary"
    
    def raise_anchor(self):
        self._anchor_dropped = False
        return "🎯 Anchor raised! Ready to move"
    
    def get_info(self):  # Polymorphism
        return f"🚢 {super().get_info()} | Type: {self.boat_type} | Length: {self.length}m"


# Motorcycle Class (Inherits from Vehicle)
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, max_speed, engine_size, style):
        super().__init__(brand, model, year, max_speed)
        self.engine_size = engine_size
        self.style = style
        self._kickstand_up = False
    
    def move(self):
        if self.get_engine_status() == "off":
            return "❌ Start the engine first!"
        if not self._kickstand_up:
            return "🛵 Raise the kickstand first!"
        return f"🏍️ Riding {self.brand} {self.model} on streets at up to {self.max_speed} km/h"
    
    def raise_kickstand(self):
        self._kickstand_up = True
        return "🦵 Kickstand raised!"
    
    def lower_kickstand(self):
        self._kickstand_up = False
        return "🦵 Kickstand lowered!"
    
    def get_info(self):  # Polymorphism
        return f"🏍️ {super().get_info()} | Engine: {self.engine_size}cc | Style: {self.style}"


# Demonstration Program
def main():
    print("🚀 VEHICLE MOVEMENT DEMONSTRATION")
    print("=" * 50)
    
    # Create different vehicles
    vehicles = [
        Car("Toyota", "Camry", 2023, 180, "Gasoline", 4),
        Airplane("Boeing", "747", 2020, 920, 68.5, 416),
        Boat("Yamaha", "242X", 2022, 45, "Speedboat", 7.3),
        Motorcycle("Harley-Davidson", "Sportster", 2023, 160, 1200, "Cruiser")
    ]
    
    # Demonstrate each vehicle
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")
        print("-" * 40)
        
        # Start engine and move
        print(vehicle.start_engine())
        
        # Vehicle-specific preparations
        if isinstance(vehicle, Car):
            print(vehicle.change_gear("D"))
        elif isinstance(vehicle, Airplane):
            print(vehicle.take_off())
        elif isinstance(vehicle, Boat):
            print(vehicle.raise_anchor())
        elif isinstance(vehicle, Motorcycle):
            print(vehicle.raise_kickstand())
        
        # Demonstrate polymorphism - same method, different behavior
        print(vehicle.move())
        
        # Show encapsulated data
        print(f"Engine Status: {vehicle.get_engine_status()}")
        
        # Vehicle-specific status
        if isinstance(vehicle, Airplane):
            print(vehicle.get_altitude())
        
        print(vehicle.stop_engine())

if __name__ == "__main__":
    main()