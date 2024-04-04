import sys  
sys.path.append("../src")

import json
import unittest
import api_startup
import operating_hours_manager

class StartupTests(unittest.TestCase): 

  def api_startup_ShouldReturnExpectedJson_WhenValidData(self):
    testManager = operating_hours_manager.Manager()
    api_startup.perform_startup_steps(testManager, "test_input_data.csv")
    result = testManager.Accessor.dataSourceAsJson
    deserializedResult = json.loads(result)

    self.assertTrue(False)
    
