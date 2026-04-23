class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, input_password):
        if self.password == input_password:
            print("Xush kelibsiz")
        else:
            print("Parol xato")


# Obyekt
user = UserLogin("ali", "1234")
user.login("1234")
user.login("0000")
