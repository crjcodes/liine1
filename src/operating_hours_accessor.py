class Accessor:
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
  what_is_open(datetime=None)
    Returns a list of operating hours filtered by the given date time
  """
  dataSourceAsJson = None

  def __init__(self, records=None):
    self.jsonRecords = records

  def what_is_open(self, datetime):
    """
    Returns a list of operating hours filtered by the given date time
    """
    return None
  
  def store(self, jsonRecords):
    self.dataSourceAsJson = jsonRecords
