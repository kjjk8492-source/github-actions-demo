import unittest

from main import convert_name_to_uppercase


class DeliberateFailureTests(unittest.TestCase):
    def test_incorrect_expected_result_fails(self) -> None:
        self.assertEqual(convert_name_to_uppercase("bob"), "BOB!")


if __name__ == "__main__":
    unittest.main()
