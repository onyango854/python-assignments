
# Assignment 1: Design Your Own Class 

# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor
        self.os = os
        self.storage = storage
        self.apps = []  # starts with no apps

    # Method to install apps
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.brand} {self.model}.")

    # Method to show phone details
    def phone_details(self):
        return f"{self.info()} | OS: {self.os} | Storage: {self.storage}GB | Apps: {self.apps}"



# Activity 2: Polymorphism Challenge 

class Animal:
    def move(self):
        pass  # placeholder for polymorphism

class Dog(Animal):
    def move(self):
        print("Running ")

class Bird(Animal):
    def move(self):
        print("Flying ")

class Fish(Animal):
    def move(self):
        print("Swimming ")


# Main Program Executio
if __name__ == "__main__":
    # --- Assignment 1 Test ---
    phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
    phone2 = Smartphone("Apple", "iPhone 14", "iOS", 128)

    phone1.install_app("WhatsApp")
    phone2.install_app("Safari")

    print(phone1.phone_details())
    print(phone2.phone_details())

    print("\n--- Polymorphism Challenge ---")
    # --- Activity 2 Test ---
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()
