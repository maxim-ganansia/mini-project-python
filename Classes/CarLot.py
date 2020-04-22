from Classes import user
from Classes import file_handler
from pathlib import Path
from Classes import log
import os


class CarLot:
    def __init__(self):
        self.user = user.User()
        self.file_handler = file_handler.FileHandler()
        self.pathUser = Path(__file__)
        self.logger = log.Logger()
        self.fleet_quantity = 0

    def update_salary_by_name(self, salary, name):
        role = self.user.user_auth(input("Please enter your name : "), input("Your password : "))
        print(role)
        if role == "admin":
            new_path = os.path.join(self.pathUser.parent.parent, "csv_files/user.csv")
            print(new_path)
            self.file_handler.load_from_csv_file(new_path)
            for x in self.file_handler.employee:
                if x["first_name"] == name:
                    employee = x
            if employee:
                employee["salary"] = str(salary)
                remove = self.file_handler.remove_from_csv(new_path, employee["id"])
                if remove == True:
                    add = self.file_handler.append_to_csv(new_path, employee)
                    if add == True:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            print("Sorry You're not an admin")
            return False

    def add_to_fleet(self, path_external):
        new_path = os.path.join(self.pathUser.parent.parent, "csv_files/vehicle.csv")
        self.file_handler.load_from_csv_file(new_path)
        originvehicle = self.file_handler.employee
        self.file_handler.load_from_csv_file(path_external)
        testvehicle = self.file_handler.employee
        if testvehicle[0].keys() == originvehicle[0].keys():
            for x in testvehicle:
                self.file_handler.add_vehicle_to_csv(new_path, x)

    def get_fleet_size(self):
        new_path = os.path.join(self.pathUser.parent.parent, "csv_files/vehicle.csv")
        self.file_handler.load_from_csv_file(new_path)
        return len(self.file_handler.employee)



Carlot = CarLot()
# Carlot.update_salary_by_name("5", "aaron")

# Carlot.add_to_fleet("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/daily "
#                    "tasks/csv_files/new_vehicles.csv")

print(Carlot.get_fleet_size())

