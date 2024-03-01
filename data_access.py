class UserDAO:
    def __init__(self):
        self.users = []
        self.current_id = 1

    def add_user(self, user):
        user.id = self.current_id
        self.users.append(user)
        self.current_id += 1
        return user.id

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update_user(self, updated_user):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                return True
        return False

    def delete_user(self, id):
        self.users = [user for user in self.users if user.id != id]

