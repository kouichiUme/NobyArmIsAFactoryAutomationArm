#  -*- coding: UTF-8 -*-
import sys
import unittest

import ObjectDistinguisher

sys.path.append("..")
class TestObjectDistinguisher(unittest.TestCase):

    def test_detect(self):
            print("detect start")
            od = ObjectDistinguisher.ObjectDistinguisher()
            od.checkObject("hogeoh")
            self.assertEqual("foo".upper(),"FOO")
        
if __name__ == '__main__':
    unittest.main()
