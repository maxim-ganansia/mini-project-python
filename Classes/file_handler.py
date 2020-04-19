import csv

from Classes import log

Logger = log.Logger


class FileHandler:
    def __init__(self):
        self.employee = []
        self.log = Logger()

    def load_from_csv_file(self, *args):
        try:
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        employee = {
                            "id": row[0],
                            "first_name": row[1],
                            "last_name": row[2],
                            "password": row[3],
                            "position": row[4],
                            "salary": row[5],
                            "role": row[6],
                        }
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
                    if row == new_keys:
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


file = FileHandler()
data = {
    "id": "23",
    "first_name": "Daryl",
    "last_name": "Mizrahi",
    "password": "12345",
    "position": "Student",
    "salary": "0",
    "role": "Student",
}
file.append_to_csv("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/Day-1 (daily "
                   "task)/csv_files/user.csv", data);

file = FileHandler()
file.load_from_csv_file("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/Day-1 (daily "
                        "task)/csv_files/user.csv")

