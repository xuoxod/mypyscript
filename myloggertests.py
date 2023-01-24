import unittest
import os
from custom_modules.MyLogger import log_this


def create_log():
    log_data = "log test"
    return log_this(log_data,"mylogger-test")


class LogCreation(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_log(self):
        results = create_log()
        print("\n\tFile Saved?\t{}\n".format(results))
        self.assertTrue(results == True)


if __name__ == "__main__":
    unittest.main()
