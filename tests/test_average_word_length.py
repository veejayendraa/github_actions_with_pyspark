import unittest
import os
from src import average_word_length
import findspark

findspark.init()

# Get the absolute path to the project's root directory
project_root = os.path.abspath(os.path.dirname(__file__))


class AverageWordLengthTestCase(unittest.TestCase):
    def test_average_word_length(self):
        input_file = os.path.join(project_root, "inputs/avg_word_length.txt")
        expected_average = 5.24  # Define the expected average word length

        # Call the function and get the result
        result = average_word_length.calculate_average_word_length(input_file)

        # Assert that the result matches the expected average
        self.assertAlmostEqual(result, expected_average, delta=0.01)


if __name__ == "__main__":
    unittest.main()
