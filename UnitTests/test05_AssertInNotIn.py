import unittest

class testAssertIn(unittest.TestCase):
    def test_CheckAssert(self):
        list1 = {"Python",".Net","Java"}
        # self.assertIn("Python",list1)
        # self.assertIn("ruby",list1)
        #self.assertNotIn("Python",list1)
        self.assertNotIn("ruby",list1)
    def test_RelationalAsserts(self):
        # self.assertGreater(19,20) #first number should be greater than second
        # self.assertGreaterEqual(20,20) #first number should b greater or equal to second 
        # self.assertLess(8,90)
        self.assertLessEqual(90,90)
        
        

if __name__ == "__main__":
    unittest.main()