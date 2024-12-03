# UserService.py
from dao.UserDAO import UserDAO


class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def authenticate_user(self, email, password):
        user = self.user_dao.get_user_by_email(email)
        if user and user.password == password:
            print("Welcome! You are now logged in!")
            return user
        else:
            print("Wrong email or password")
            return None

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_user_by_email(self, email):
        # Query database for a user with the provided email
        # Return user object or None if not found
        pass

    def create_user(self, firstname, lastname, email, password):
        # Save the new user to the database
        # Make sure to hash the password before saving
        pass
