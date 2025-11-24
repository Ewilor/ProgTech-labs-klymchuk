
import unittest
from grades_management import add_child, calcucale_avg

class TestSchoolInfoAutomation(unittest.TestCase):
    def test_add_child_success(self):
        data = {}
        child = ("8-A", "Test T.T.")
        count = add_child(data, child)
        self.assertEqual(count, 1)

    def test_add_child_duplicate(self):
        data = {("8-A", "Test T.T."): {}}
        child = ("8-A", "Test T.T.")
        with self.assertRaises(ValueError) as context:
            add_child(data, child)
        self.assertEqual(str(context.exception), "Учень вже існує у словнику")

    def test_calcucale_avg_success(self):
        data = {("6-A", "Test T.T."): {"Math": [10, 12, 8]}}
        avg = calcucale_avg(data, ("6-A", "Test T.T."), "Math")
        self.assertEqual(avg, 10)

    def test_calcucale_avg_no_subject(self):
        data = {("6-A", "Test T.T."): {"Math": [10, 12, 8]}}
        avg = calcucale_avg(data, ("6-A", "Test T.T."), "Physics")
        self.assertEqual(avg, -1)

    def test_calcucale_avg_no_child(self):
        data = {("6-A", "Test T.T."): {"Math": [10, 12, 8]}}
        with self.assertRaises(ValueError) as context:
            calcucale_avg(data, ("7-B", "No Name"), "Math")
        self.assertEqual(str(context.exception), "Учня не знайдено у словнику")

if __name__ == "__main__":
    unittest.main()
