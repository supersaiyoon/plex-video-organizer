import unittest

from main import is_ignored_dir

class TestMain(unittest.TestCase):
    def test_is_ignored_dir(self):
        self.assertEqual(is_ignored_dir("anime"), True)
        self.assertEqual(is_ignored_dir("movies"), True)
        self.assertEqual(is_ignored_dir("stand-up comedy"), True)
        self.assertEqual(is_ignored_dir("tv shows"), True)