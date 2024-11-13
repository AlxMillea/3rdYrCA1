from model.User import User


class UserDAO:
    def __init__(self):
        # Initialize with some dummy users
        self.users = [
            User(2, "John", "Doe", "john@example.com", "password123", "customer"),

            User(1, "Jane", "Admin", "jane@example.com", "admin_password", "admin")
        ]

    def get_all_users(self):
        return self.users

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
