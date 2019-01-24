import unittest
import random


class GuessTest(unittest.TestCase):
    def TestSetUp(self):
        #Setup variables. This runs before every test method.
        self.number = random.randint(1, 20)
    # end setUp
   

    def test_other_method(self):
        pass

    def tearDown(self):
        #This runs after every test is finished.
        # If you have to clean up something
        pass
    # end tearDown
# end class GuessTest

if __name__ == "__main__":
    # Code that runs when you run this file, so importing this file doesn't run your code
    # CheckGuess() # Run your function

    unittest.main() # Run the unittests
