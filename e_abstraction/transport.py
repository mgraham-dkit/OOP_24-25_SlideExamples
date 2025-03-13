from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"


class MotorBike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"