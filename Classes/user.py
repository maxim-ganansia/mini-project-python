from Classes import file_handler
from Classes import log

FileHandler = file_handler.FileHandler
Logger = log.Logger

class User:
    def __init__(self):
        self.result = FileHandler()
        self.log = Logger()

    def user_auth(self, name, password):
        try:
            self.result.load_from_csv_file(
                "/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/Day-1 (daily "
                "task)/csv_files/user.csv")
            for x in self.result.employee:
                if x["first_name"] == name and x["password"] == password:
                    self.log.add_to_log(" We search user with first name and password""\n")
                    return x["role"]
            return False

        except Exception as error:
            print("There is an error : " + str(error))
            self.log.add_to_log(" We search user with first name and password but there is an error""\n")

user = User()
role = user.user_auth("amir", "12345678")
print(role)
