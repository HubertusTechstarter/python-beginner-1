import unittest
import exercises  # Assuming exercises.py is in the same directory

class TestVariableAssignments(unittest.TestCase):
    
    def test_exercise_1(self):
        try:
            self.assertEqual(exercises.x, 5)
        except AttributeError:
            self.fail("Exercise 1 failed: 'x' is not defined. Please declare a variable named 'x' and assign the value 5 to it.")
        except AssertionError:
            self.fail("Exercise 1 failed: The value of 'x' is incorrect. It should be 5.")
    
    def test_exercise_2(self):
        try:
            self.assertEqual(exercises.y, 10)
        except AttributeError:
            self.fail("Exercise 2 failed: 'y' is not defined. Please declare a variable named 'y' and assign the value 10 to it.")
        except AssertionError:
            self.fail("Exercise 2 failed: The value of 'y' is incorrect. It should be 10.")
    
    def test_exercise_3(self):
        try:
            self.assertEqual(exercises.z, 15)
        except AttributeError:
            self.fail("Exercise 3 failed: 'z' is not defined. Please declare a variable named 'z' and assign the value 15 to it.")
        except AssertionError:
            self.fail("Exercise 3 failed: The value of 'z' is incorrect. It should be 15.")
    
    def test_exercise_4(self):
        try:
            self.assertEqual(exercises.a, 20)
        except AttributeError:
            self.fail("Exercise 4 failed: 'a' is not defined. Please declare a variable named 'a' and assign the value 20 to it.")
        except AssertionError:
            self.fail("Exercise 4 failed: The value of 'a' is incorrect. It should be 20.")
    
    def test_exercise_5(self):
        try:
            self.assertEqual(exercises.b, 25)
        except AttributeError:
            self.fail("Exercise 5 failed: 'b' is not defined. Please declare a variable named 'b' and assign the value 25 to it.")
        except AssertionError:
            self.fail("Exercise 5 failed: The value of 'b' is incorrect. It should be 25.")

if __name__ == '__main__':
    unittest.main()
