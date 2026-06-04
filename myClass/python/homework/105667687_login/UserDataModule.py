from datetime import datetime

class UserData:

    def __init__(self, user_data) -> None:
        self.username = user_data[0]
        self.passwd = user_data[1]
        self.email = user_data[2]
        self.name = user_data[3]
        self.mail_ready = bool(user_data[4])
        self.mail_number = int(user_data[5])
        self.account_created = datetime.strptime(user_data[6], "%Y-%m-%d %H:%M:%S%z")
        self.mail_check_time = datetime.strptime(user_data[7], "%Y-%m-%d %H:%M:%S%z")
        self.__pass_count:int = 0

    def set_pass_count(self):
        self.__pass_count += 1

    def get_pass_count(self):
        return self.__pass_count

    
