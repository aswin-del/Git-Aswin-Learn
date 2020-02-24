import unittest
import AswinCalc


class MyTestCase(unittest.TestCase):
    def test_add( self ):
        self.assertEqual(AswinCalc.add(10, 5), 10 )


if __name__ == '__main__':
    unittest.main()
