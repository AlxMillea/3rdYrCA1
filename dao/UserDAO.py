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

    def create_user(self, firstname, lastname, email, password, role="customer"):
        # Check if user already exists
        if self.get_user_by_email(email):
            return False  # User already exists

        # Create a new user with an auto-incremented ID
        new_id = max(user.id for user in self.users) + 1 if self.users else 1
        new_user = User(new_id, firstname, lastname, email, password, role)
        self.users.append(new_user)
        return True  # User successfully created
