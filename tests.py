import unittest

from main import convert_name_to_uppercase


class ConvertNameToUppercaseTests(unittest.TestCase):
    def test_converts_lowercase_name(self) -> None:
        self.assertEqual(convert_name_to_uppercase("alice"), "ALICE")

    def test_converts_mixed_case_name(self) -> None:
        self.assertEqual(convert_name_to_uppercase("mArY Jane"), "MARY JANE")

    def test_empty_name_stays_empty(self) -> None:
        self.assertEqual(convert_name_to_uppercase(""), "")


if __name__ == "__main__":
    unittest.main()