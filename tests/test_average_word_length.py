import unittest

from average_word_length import calculate_average_word_length
import findspark
findspark.init()

class AverageWordLengthTestCase(unittest.TestCase):
    def test_average_word_length(self):
        input_file = "inputs/avg_word_length.txt"
        expected_average = 5.25  # Define the expected average word length

        # Call the function and get the result
        result = calculate_average_word_length(input_file)

        # Assert that the result matches the expected average
        self.assertAlmostEqual(result, expected_average, delta=0.01)

if __name__ == "__main__":
    unittest.main()
