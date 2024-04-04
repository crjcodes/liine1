import string
import datetime
import re
from operating_hours import OperatingHours

def ConvertFrom(filename):
  """
  Takes the name of a csv file matching the business specification, then
  maps to a list of our internal data model
  DESIGN: mapping to a data model may be overkill. Can just map to a json structure
  and treat it like a database of sorts
  """
  if not filename or not filename.strip():
    # TODO: FUTURE: configurable logging
    raise ValueError()

  file = open(filename, "r")
  # Assuming always a header
  next(file)

  for line in file:
    print(f"line is [{line}]")
    field_values = line.split(',')

    if not ValidateRestaurantData(field_values):
      raise ValueError()     
    
    restaurant_name = field_values[0]
    opHours = ParseOpHours(field_values[1])

  return ""

def ValidateRestaurantData(field_values):
  if field_values == None:
    print("No data found in this line")
    return False
  
  if isinstance(field_values, list) == False:
    print("Data not recognized")
    return False
  
  length = len(field_values)
  if not field_values or length != 2:
    print("Not all fields were found in this row of data")
    return False
 
  return True

def ParseOpHours(human_readable_op_hours):
  """
  TODO: 
    Future: if performance concerns, compile the regex
      beforehand (plus other options)
    Future: the find/replace can be replaced by one operation
  """
  sections = human_readable_op_hours.split(r'\s*/\s*')

  op_hours_list = []

  for section in sections:
    dowPattern = "(Mon|Tue|Wed|Thu|Fri|Sat|Sun)"

    beginning_dow = findFirst(f"/^{dowPattern}-/i", section)
    ending_dow = findFirst(f"/-{dowPattern}/i", section)

    if beginning_dow == "" or ending_dow == "":
      # FUTURE: log
      continue

    re.sub(f"-*{dowPattern}-*", "", section)
    hours = section.split(r'\s*-\s*')

    if not hours or len(hours) != 2:
      # FUTURE: log
      continue

    start_time = datetime.datetime.strptime(hours[0], '%H:%M').time()
    end_time = datetime.datetime.strptime(hours[1], '%H:%M').time()

    # TODO: move to a constant list
    for dow in "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun":
      op_hours = OperatingHours(dow, start_time, end_time)
      op_hours_list.append(op_hours)

  return op_hours_list

def findFirst(pattern, text):
  find = re.findall(pattern, text)
  if not find or len(find) == 0:
    return None
  
  return find[0]

