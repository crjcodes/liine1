import sys  
sys.path.append("../src")

import unittest
import convert_engine

class ConvertTests(unittest.TestCase):
  def test_ParseLastTimeText_ShouldReturnTimeAsText_WhenGivenSampleData(self):
    testData = "Mon-Thu, Sun 11 am - 10 pm"
    modifiedTestData, timeText = convert_engine.ParseLastTimeText(testData)
    self.assertIsNotNone(timeText)
    self.assertEqual("10pm", timeText)

  # def test_convert_from_returns_true(self):
  #   result = convert_engine.ConvertFrom("test_input_data.csv")
  #   self.assertTrue(result)
  #   return
    
  def test_ParseLastTimeText_ShouldReturnEndAndOpenTimeAsText_WhenGivenSampleData(self):
    """
    More of a "sequence" test than a unit test
    """

    testData = "Mon-Thu, Sun 11 am - 10 pm"

    modifiedTestData, timeText = convert_engine.ParseLastTimeText(testData)

    self.assertIsNotNone(timeText)
    self.assertEqual("10pm", timeText)
    self.assertEqual("Mon-Thu, Sun 11 am", modifiedTestData)

    modifiedTestData, timeText = convert_engine.ParseLastTimeText(modifiedTestData)
    self.assertIsNotNone(timeText)
    self.assertEqual("11am", timeText)
    self.assertEqual("Mon-Thu, Sun ", modifiedTestData)

  def test_ParseDowText_ShouldReturnExpectedListofDaysOfWeek_WhenGivenSampleData(self):
     testData = "Mon-Thu, Sun "
     result = convert_engine.ParseDowText(testData)

     self.assertIsNone(result)
     self.assertIsInstance(result, list)
     self.assertEqual("Mon", list[0])
     self.assertEqual("Tue", list[1])
     self.assertEqual("Wed", list[2])
     self.assertEqual("Thu", list[3])
     self.assertEqual("Sun", list[4])


if __name__ == '__main__':
    unittest.main()    
    