import unittest
from unittest.mock import mock_open, patch


class Logger:
    def __init__(self, filepath):
        self.filepath = filepath

    def log(self, message):
        with open(self.filepath, "a") as file:
            file.write(f"{message}\n")


class TestLogger(unittest.TestCase):
    def test_log(self):
        message = "Hello, logging world!"

        mocked_open = mock_open()

        with patch("builtins.open", mocked_open):
            logger = Logger("dummy_path.log")
            logger.log(message)

            # Check that open was called correctly
            mocked_open.assert_called_once_with("dummy_path.log", "a")

            # Check that the write method was called with the correct message
            mocked_open().write.assert_called_once_with(f"{message}\n")


if __name__ == "__main__":
    unittest.main()
