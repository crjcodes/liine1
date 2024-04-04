import string
import convert_engine
import operating_hours_accessor

class Manager:
  Accessor = operating_hours_accessor.Accessor()

  """
  Manages the use cases for requesting what establishments are open
  """
  def list_operating_restaurants(self, date_time=None):
    return "TODO"

  def ingest_new_data_source(self, filename):
    Converted = convert_engine.ConvertFrom(filename)
    self.Accessor.store(Converted)
    return
  
  def parse_dow_start_end(self, line):
    return