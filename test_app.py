import unittest
import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        database.init_db()
        self.emp_id = database.add_employee("Test User", "Engineer")

    def test_add_and_get(self):
        employees = database.get_employees()
        self.assertTrue(any(emp['name'] == "Test User" for emp in employees))

    def test_delete_employee(self):
        result = database.delete_employee(self.emp_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
