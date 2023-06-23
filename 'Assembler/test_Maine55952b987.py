# Test generated by RoostGPT for test roost-test using AI Model vertex

import unittest

from __future__ import print_function
import sys


class TestMain(unittest.TestCase):

    def test_main_no_arguments(self):
        """
        Test that the program exits with an error message when no arguments are passed.
        """
        with self.assertRaises(SystemExit):
            main()

    def test_main_one_argument(self):
        """
        Test that the program loads the file specified by the argument and interprets it.
        """
        with open("test.txt", "w") as f:
            f.write("print('Hello, world!')")

        main("test.txt")

        self.assertEqual(print("Hello, world!"), None)


if __name__ == "__main__":
    unittest.main()