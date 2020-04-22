import csv
import collections
from Classes import log

Logger = log.Logger


class FileHandler:
    def __init__(self):
        self.employee = []
        self.log = Logger()
        self.collections = collections

    def load_from_csv_file(self, *args):
        try:
            employee = {}
            self.employee = []
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        header = row
                        line_count += 1
                    else:
                        i = 0
                        employee = {}
                        for x in header:
                            employee[x] = row[i]
                            i += 1
                        self.employee.append(employee)
                self.log.add_to_log(" We went through the csv file user""\n")

        except Exception as error:
            print("There is an error : " + str(error))
            self.log.add_to_log(" We tried to go through the csv file user but there is an error""\n")

    def append_to_csv(self, path, data):
        new_keys = []
        for key in data.keys():
            new_keys.append(key)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    if self.collections.Counter(row) == self.collections.Counter(new_keys):
                        line_count += 1
                    else:
                        return False
                else:
                    if data["id"] == row[0]:
                        return False
        with open(path, "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([data["id"], data["first_name"], data["last_name"], data["password"],
                                 data["position"], data["salary"], data["role"]])
            self.log.add_to_log(" We added a new person to csv file user""\n")

    def remove_from_csv(self, path, id):
        lines = list()
        value = False
        try:
            with open(path, "r") as read:
                reader = csv.reader(read)
                for row in reader:
                    if row[0] != id:
                        lines.append(row)
                    else:
                        value = True
            with open(path, "w", newline="") as write:
                writer = csv.writer(write)
                writer.writerows(lines)
                self.log.add_to_log(" We deleted the row with same id""\n")
            return value

        except Exception as e:
            print("there was an error" + str(e))

    def update_csv(self, path, id, row):
        value = self.remove_from_csv(path, id)
        if value == True:
            row["id"] = str(id)
            self.append_to_csv(path, row)

    def add_vehicle_to_csv(self, path, data):
        self.load_from_csv_file(path)
        for x in self.employee:
            if x["id"] == data["id"]:
                return False
        with open(path, "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            new_row = [data["id"], data["brand"], data["owner"], data["last_test"], data["color"], data["door_count"]]
            csv_writer.writerow(new_row)
            return True


file = FileHandler()
data = {
    "id": "33",
    "first_name": "aaron",
    "last_name": "Cohen",
    "password": "12345",
    "position": "Student",
    "salary": "0",
    "role": "admin",
}
# file.append_to_csv("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/daily "
#                   "tasks/csv_files/user.csv", data)

#file = FileHandler()
#file.load_from_csv_file("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/daily "
#                    "tasks/csv_files/user.csv")

# file.remove_from_csv("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/daily "
#                     "tasks/csv_files/user.csv", "25")

# row = {
#     "first_name": "Elie",
#     "last_name": "Benpapa",
#     "password": "12345",
#     "position": "Student",
#     "salary": "1k",
#     "role": "Student"
# }
#
# file.update_csv("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/daily "
#                 "tasks/csv_files/user.csv", "24", row)

