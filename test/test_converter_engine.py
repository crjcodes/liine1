import sys  
sys.path.append("../src")

import converter_engine

class ConvertTests:
  def test_convert_from_returns_true(self):
    result = converter_engine.ConvertFrom("myfile")
    self.assertTrue(result)
    