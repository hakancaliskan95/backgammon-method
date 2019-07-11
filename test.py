import unittest
import sys
import backgammon

class test_moves(unittest.TestCase):
    
    checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
    dice1=4
    dice2=2
    positiion1=6
    position2=10
    
    def runTest(self):
        result = backgammon.find_moves(self.checkers, self.dice1, self.dice2)
        print("First positions =>",self.checkers,"\nDices=>",self.dice1,self.dice2,"\nPossible Moves=>",result)
        
    checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
    dice1=7
    dice2=2
    positiion1=6
    position2=10
    
    def runTest2(self):
        result = backgammon.find_moves(self.checkers, self.dice1, self.dice2)
        print("First positions =>",self.checkers,"\nDices=>",self.dice1,self.dice2,"\nPossible Moves=>",result)
  
if __name__ == "__main__":
    unittest.main()