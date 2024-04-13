class VkAccount:
    def __init__(self, name, login_id, password):
        self.name = name
        self.login_id = login_id
        self.password = password

    def login(self):
        if self.login_id == 'id' and self.password == 'password':
            pass
            return True

