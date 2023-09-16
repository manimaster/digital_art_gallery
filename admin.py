# (c) 2018 Manikandan

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'Admin Username: {self.username}'
