from Models.Car import Car
from Repository.Car_repo import Car_repo
import os

class Car_service(Car):
    def __init__(self):
        self.car_info = ["Plate_number","Car","Transmission","Seats","Color","Doors","Suit_cases", \
        "Fuel_type","Year","Price","Insurance", "Status", "Kilometers", "CO2", "Highlander"]
        self.car_list = []
        self.car_write = Car_repo()
        self.all_cars = Car_repo()

    def car_main_info_to_list(self):
        for info in self.car_info[:11]:
            os.system('cls||clear')
            if info == "Transmission":
                print(info)
                print("\t1. Manual")
                print("\t2. Automatic")
                choice = input("Choose an option: ")
                if choice == "1":
                    self.car_list.append("Manual")
                elif choice == "2":
                    self.car_list.append("Automatic")
            else:
                item = input("{}: ".format(info))
                self.car_list.append(item)

    def car_addit_info_to_list(self):
        for info in self.car_info[11:]:
            os.system('cls||clear')
            item = input("{}: ".format(info))
            self.car_list.append(item)

    def print_new_car_info(self):
        for i in range(len(self.car_list)):
            print("{}: {}".format(self.car_info[i], self.car_list[i]))
            if i // 2 == 0:
                print("\t")

    def add_car_to_repo(self):
        self.car_write.write_to_file(self.car_list)
    
    def get_all_cars(self):
        cars_list = []  # Frikki commenta
        get_car_info_val = self.all_cars.read_car_data()
        for car in get_car_info_val:
            car_dict = {}
            for i in range(len(car)):
                car_dict[self.car_info[i]] = car[i]
            cars_list.append(car_dict)

        return cars_list
    
    def get_available_cars(self):
        self.cars_list = Car_service()
        get_available_cars = []
        all_cars = self.cars_list.get_all_cars()
        for car in all_cars:
            for key in car.keys():
                if car[key] == "available":
                    get_available_cars.append(car)
        
        return get_available_cars




