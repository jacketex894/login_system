import unittest
from datetime import datetime

from ..lib.DataBase import UserDB,UserData

class TestUserDB(unittest.TestCase):
    def setUp(self):
        self.request_data: UserData = {
            "user_name": "test_user",
            "password": "test_password",
            "mail": "test_mail@example.com",
            "created_at": datetime.now(),  
            "last_login_ip": "127.0.0.1"
        }
    def test_register(self):
        UserDB.register_user(self.request_data)
        retrieved_user = UserDB.query_user(self.request_data["user_name"])
        self.assertIsNotNone(retrieved_user, "retrieved_user should not be None")
        self.assertEqual(retrieved_user.user_name, self.request_data["user_name"])

    def test_update(self):
        update_mail = "update_mail@example.com"
        update_password = "update_password"
        UserDB.update_user(self.request_data["user_name"],update_password,update_mail)
        updated_user = UserDB.query_user(self.request_data["user_name"])
        self.assertEqual(updated_user.mail, update_mail)
        self.assertEqual(updated_user.password, update_password)


    def test_delete(self):
        retrieved_user = UserDB.query_user(self.request_data["user_name"])
        UserDB.delete_user(retrieved_user)
        deleted_user = UserDB.query_user(self.request_data["user_name"])
        self.assertIsNone(deleted_user, "deleted_user should be None")

if __name__ == '__main__':
    unittest.main()