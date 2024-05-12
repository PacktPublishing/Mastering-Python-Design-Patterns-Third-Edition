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
        msg = "Hello, logging world!"

        m_open = mock_open()

        with patch("builtins.open", m_open):
            logger = Logger("dummy.log")
            logger.log(msg)

            m_open.assert_called_once_with(
                "dummy.log", "a"
            )
            m_open().write.assert_called_once_with(
                f"{msg}\n"
            )


if __name__ == "__main__":
    unittest.main()
