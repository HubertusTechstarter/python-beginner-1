import unittest
import exercises  # Assuming exercises.py is in the same directory

class TestVariableAssignments(unittest.TestCase):
    
    def test_exercise_1(self):
        # Check if 'x' is defined
        self.assertTrue(hasattr(exercises, 'x'), "Exercise 1 failed: 'x' is not defined.")
        # Check if 'x' has the correct value
        self.assertEqual(exercises.x, 5, "Exercise 1 failed: The value of 'x' should be 5.")
    
    # def test_exercise_2(self):
    #     # Check if 'y' is defined
    #     self.assertTrue(hasattr(exercises, 'y'), "Exercise 2 failed: 'y' is not defined.")
    #     # Check if 'y' has the correct value
    #     self.assertEqual(exercises.y, 10, "Exercise 2 failed: The value of 'y' should be 10.")
    
    # def test_exercise_3(self):
    #     # Check if 'z' is defined
    #     self.assertTrue(hasattr(exercises, 'z'), "Exercise 3 failed: 'z' is not defined.")
    #     # Check if 'z' has the correct value
    #     self.assertEqual(exercises.z, 15, "Exercise 3 failed: The value of 'z' should be 15.")
    
    # def test_exercise_4(self):
    #     # Check if 'a' is defined
    #     self.assertTrue(hasattr(exercises, 'a'), "Exercise 4 failed: 'a' is not defined.")
    #     # Check if 'a' has the correct value
    #     self.assertEqual(exercises.a, 20, "Exercise 4 failed: The value of 'a' should be 20.")
    
    # def test_exercise_5(self):
    #     # Check if 'b' is defined
    #     self.assertTrue(hasattr(exercises, 'b'), "Exercise 5 failed: 'b' is not defined.")
    #     # Check if 'b' has the correct value
    #     self.assertEqual(exercises.b, 25, "Exercise 5 failed: The value of 'b' should be 25.")

if __name__ == '__main__':
    unittest.main()