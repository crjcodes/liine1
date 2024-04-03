import converter_engine
import operating_hours_accessor

class Manager:
  Accessor = operating_hours_accessor.Accessor()

  """
  Manages the use cases for requesting what establishments are open
  """
  def list_operating_restaurants(self, date_time=None):
    return "TODO"

  def ingest_new_data_source(self, filename):
    # validation: just inside manager; no need for separate validation engine
    Converted = converter_engine.ConvertFrom(filename)
    Success = self.Accessor.store(Converted)
    return 
