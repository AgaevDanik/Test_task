import unittest
from main import Frame


class TestFrame(unittest.TestCase):
    def setUp(self) -> None:
        self.A = Frame(['test', 'testtest'], '*', 'test')

    def test_get_max_len(self):
        self.assertEqual(self.A.get_max_len(), 8)

    def test_get_a_border_width(self):
        self.assertEqual(self.A.get_a_border_width(), 12)

    def test_get_delta(self):
        self.assertEqual(self.A.get_delta('test'), 4)

    def test_make_content_row(self):
        self.assertEqual(self.A.make_content_row('test'), '* test     *')


if __name__ == '__main__':
    unittest.main()
