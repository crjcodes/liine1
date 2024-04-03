class OperatingHoursAccessor:
  """
  Represents the class that talks to our data.
  In this case, just a large json string, but in real-life situations, 
  this would be talking to whatever resource makes sense, whether
  MS-SQL, Redis, Graph database, etc

  ...
  Attributes
  records : list of OperatingHour
    represents the internal model of the data

  Methods
  includes(datetime=None)
    Returns a list of operating hours filtered by the given date time
  """
  def __init__(self, records=None):
    self.records = records

  def includes(datetime):
    """
    Returns a list of operating hours filtered by the given date time
    """
    return None
  
  def addConvertedData(listOfRecords):
    return None