from abc import ABC, abstractmethod
class vehicle(ABC):

    @abstractmethod
    def calculate_toll(self,person):
        pass

## Two Wheeler

class TwoWheeler(vehicle):
    def calculate_toll(self,persons):

        basic_toll = 20

        if persons >2:
            extra_charge = (persons - 2)* 10

        else:
            extra_charge = 0

        total = basic_toll + extra_charge

        return total


### Three wheeler (vehicle)

class ThreeWheeler(vehicle):
    def calculate_toll(self,persons):

        basic_toll = 30

        if persons > 3:
            extra_charge = (persons - 3) * 20

        else:
            extra_charge = 0

        total = basic_toll + extra_charge

        return total


## Four Wheeler

class FourWheeler(vehicle):
    def calculate_toll(self,persons):

        basic_toll = 40

        if persons >4:
             extra_charge = (persons - 4) * 40
  
        else:
            extra_charge = 0

        total = basic_toll + extra_charge

        return total


# Heavy vehicle

class HeavyVehicle(vehicle):
    def calculate_toll(self,persons):

        basic_toll = 60

        if persons >2:
             extra_charge = (persons - 6) * 100

        else:
            extra_charge = 0

        total = basic_toll + extra_charge

        return total
def main():

    while True:

        print("\n===== TOLL TAX SYSTEM =====")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 5:
                print("Thank you for using Toll System!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice!")
                continue

            persons = int(input("Enter number of persons: "))

            if persons <= 0:
                print("Enter a valid number of persons!")
                continue

            if choice == 1:
                vehicle = TwoWheeler()

            elif choice == 2:
                vehicle = ThreeWheeler()

            elif choice == 3:
                vehicle = FourWheeler()

            elif choice == 4:
                vehicle = HeavyVehicle()

            # Polymorphism
            total_toll = vehicle.calculate_toll(persons)

            print("--------------------------")
            print("Total Toll: Rs.", total_toll)
            print("--------------------------")

        except ValueError:
            print("Please enter numbers only!")


main()     