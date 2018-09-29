#  -*- coding: UTF-8 -*-
import sys
import unittest

import NobyNeckMoverGimbalStorm

sys.path.append("..")
class TestNobyNeckMoverGimbalStorm(unittest.TestCase):

    def test_detect(self):
            print("noby neck mover start")
            nobyNeck = NobyNeckMoverGimbalStorm.NobyNeckMoverGimbalStorm()
            nobyNeck.move(20,20,20)
            self.assertEqual("foo".upper(),"FOO")
        
if __name__ == '__main__':
    unittest.main()
