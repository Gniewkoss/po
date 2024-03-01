import unittest
from app import app
from data_access import UserDAO
from models import User


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_dao = UserDAO()

    def tearDown(self):
        self.user_dao.users = []

    def test_get_users(self):
        user = User("John", "Doe", 1990, "user")
        self.user_dao.add_user(user)


    def test_create_user(self):
        user_data = {
            "firstName": "Test",
            "lastName": "User",
            "birthYear": 1990,
            "group": "user"
        }



    def test_get_user(self):
        user = User("John", "Doe", 1990, "user")
        user_id = self.user_dao.add_user(user)





if __name__ == '__main__':
    unittest.main()
