import sys  
sys.path.append("../src")

import unittest
import converter_engine

class ConvertTests(unittest.TestCase):
  def test_convert_from_returns_true(self):
    result = converter_engine.ConvertFrom("test_input_data.csv")
    self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()    
    