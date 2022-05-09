import os
import unittest

from pylabview_helpers import vi

this_dir = os.path.dirname(os.path.realpath(__file__))

class TestVI(unittest.TestCase):
    def test_can_parse_vi(self):
        vi_obj = vi.get_vi(os.path.join(this_dir, "add.vi"))
        assert vi_obj is not None