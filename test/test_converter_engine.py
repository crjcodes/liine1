import sys  
sys.path.append("../src")

import unittest
import convert_engine

class ConvertTests(unittest.TestCase):

#region parse_last_time_text
  
  # TODO: use input test data into one test, not two sets in sequence
  def test_parse_last_time_text_ShouldReturnNone_WhenInvalidInput(self):
    modifiedTestData, timeText = convert_engine.parse_last_time_text("")
    self.assertIsNone(timeText)
    self.assertEqual("", modifiedTestData)

    modifiedTestData, timeText = convert_engine.parse_last_time_text("blah blah")
    self.assertIsNone(timeText)
    self.assertEqual("blah blah", modifiedTestData)

  def test_parse_last_time_text_ShouldReturnTimeAsText_WhenGivenSampleData(self):
    testData = "Mon-Thu, Sun 11 am - 10 pm"
    modifiedTestData, timeText = convert_engine.parse_last_time_text(testData)
    self.assertIsNotNone(timeText)
    self.assertEqual("10pm", timeText)
    
  def test_parse_last_time_text_ShouldReturnEndAndOpenTimeAsText_WhenGivenSampleData(self):
    """
    More of a "sequence" test than a unit test
    """

    testData = "Mon-Thu, Sun 11 am - 10 pm"

    modifiedTestData, timeText = convert_engine.parse_last_time_text(testData)

    self.assertIsNotNone(timeText)
    self.assertEqual("10pm", timeText)
    self.assertEqual("Mon-Thu, Sun 11 am", modifiedTestData)

    modifiedTestData, timeText = convert_engine.parse_last_time_text(modifiedTestData)
    self.assertIsNotNone(timeText)
    self.assertEqual("11am", timeText)
    self.assertEqual("Mon-Thu, Sun ", modifiedTestData)
#endregion

#region parse_dow_text
  # TODO: break apart into test cases with parameterized test data
  def test_parse_dow_text_ShouldReturnExpectedListofDaysOfWeek_WhenGivenBadData(self):
     testData = "Mon-Thu, TBD "
     result = convert_engine.parse_dow_text(testData)

     self.assertIsNotNone(result)
     self.assertIsInstance(result, list)
     self.assertEqual("Mon", result[0])
     self.assertEqual("Tue", result[1])
     self.assertEqual("Wed", result[2])
     self.assertEqual("Thu", result[3])

     testData = "TBD-Thu, Sun"
     result = convert_engine.parse_dow_text(testData)

     self.assertEqual("Sun", result[0])

     testData = "Mon-TBD, Sun"
     result = convert_engine.parse_dow_text(testData)

     self.assertEqual("Sun", result[0])

  def test_parse_dow_text_ShouldReturnExpectedListofDaysOfWeek_WhenGivenSampleData(self):
     testData = "Mon-Thu, Sun "
     result = convert_engine.parse_dow_text(testData)

     self.assertIsNotNone(result)
     self.assertIsInstance(result, list)
     self.assertEqual("Mon", result[0])
     self.assertEqual("Tue", result[1])
     self.assertEqual("Wed", result[2])
     self.assertEqual("Thu", result[3])
     self.assertEqual("Sun", result[4])
#endregion




if __name__ == '__main__':
    unittest.main()    
    