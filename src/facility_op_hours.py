class FacilityOpHours:
  """
  Internal data model representing a facility and its hours of operation
  The hours of operation will be a list where each element is OperatingHours
  aka a day of week, a start time, and a close time
  """
  def __init__(self, name, op_hours):
      self.facility_name = name
      self.list_op_hours = list(op_hours)
