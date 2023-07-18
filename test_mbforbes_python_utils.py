import unittest
from mbforbes_python_utils import flatten

class TestMBForbesPythonUtils(unittest.TestCase):
    def test_flatten(self):
        worklist = [
            # should not un-list non-nested lists
            ([1, 2, 3], [1,2,3]),
            # test various nestings
            ([[1, 2, 3]], [1,2,3]),
            ([[[1, 2, 3]]], [1,2,3]),
            ([[[[1], [2, 3]]]], [1,2,3]),
            ([[[[1], [2, [3]]]]], [1,2,3]),
        ]
        for (input, expected) in worklist:
            self.assertEqual(flatten(input), expected)

if __name__ == '__main__':
    unittest.main()
