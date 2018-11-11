#  -*- coding: UTF-8 -*-
import sys
import unittest

import NobyNeckMoverGimbalStorm

sys.path.append("..")
class TestNobyNeckMoverGimbalStorm(unittest.TestCase):

    def test_storm(self):
            print("noby neck mover start")
            nobyNeck = NobyNeckMoverGimbalStorm.NobyNeckMoverGimbalStorm()
            nobyNeck.moveRotate(20,20,20)
            self.assertEqual("foo".upper(),"FOO")
        
if __name__ == '__main__':
    unittest.main()
