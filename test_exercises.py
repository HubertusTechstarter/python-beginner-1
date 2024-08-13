import unittest
import exercises  # Assuming the exercises are in a file named exercises.py

class TestVariableAssignments(unittest.TestCase):
    
    def test_exercise_1(self):
        self.assertEqual(exercises.x, 5, "Exercise 1 failed: 'x' should be 5.")
    
    def test_exercise_2(self):
        self.assertEqual(exercises.y, 10, "Exercise 2 failed: 'y' should be 10.")
    
    def test_exercise_3(self):
        self.assertEqual(exercises.z, 15, "Exercise 3 failed: 'z' should be 15.")
    
    def test_exercise_4(self):
        self.assertEqual(exercises.a, 20, "Exercise 4 failed: 'a' should be 20.")
    
    def test_exercise_5(self):
        self.assertEqual(exercises.b, 25, "Exercise 5 failed: 'b' should be 25.")

if __name__ == '__main__':
    unittest.main()
