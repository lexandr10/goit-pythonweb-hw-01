from abc import ABC, abstractmethod

class Vahicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vahicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vahicle):

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self,make, model):
        pass

    @abstractmethod
    def create_motorcycle(self,make,model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = eu_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()


vehicle2 = us_factory.create_car("Ford", "Mustang")
vehicle2.start_engine()
