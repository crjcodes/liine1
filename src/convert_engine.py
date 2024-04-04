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
    result = MapLineToModel(line)

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

def MapLineToModel(line):
  """
  Will return the sub-json to add to our data "store"
  """
  print(f"line is [{line}]")

  line = line.strip()
  field_values = line.split(',')

  if not ValidateRestaurantData(field_values):
    raise ValueError()     
  
  restaurant_name = field_values[0]
  opHours = ParseOpHours(field_values[1])

  return


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
    section, close_time_text = ParseLastTimeText(section) 
    section, open_time_text = ParseLastTimeText(section)
    
    dowList = ParseDow(section)

    start_time = datetime.datetime.strptime(open_time_text, '%H:%M').time()
    end_time = datetime.datetime.strptime(close_time_text, '%H:%M').time()

    # TODO: move to a constant list
    for dow in "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun":
      op_hours = OperatingHours(dow, start_time, end_time)
      op_hours_list.append(op_hours)

  return op_hours_list

def ParseLastTimeText(section):
  
  # non-overlapping
  # look for the last occurrence first
  # TODO: FUTURE: possible performance improvements with a different search, if needed
  match = re.search(r"(?s:.*)\s([0-9][0-9:]*\s*[ap]m)\s*", section)
  timeText = match.group(1)
  section = section.replace(timeText, "")
  # TODO: as regex, in case spaces aren't there
  section = section.replace(" - ", "")
  print(f"section = {section}")

  # TODO: error check on the match results
  return section, re.sub(r'\s', "", timeText)

def ParseDowText(section):
    # TODO: move to common location
    dow_full = "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    dow_list = []

    # disconnected days
    firstBreak = section.split(",")
    for f in firstBreak:
      second_break = f.split("-")      
      start_dow = second_break[0].strip()
      dow_list.append(start_dow)
      
      if len(second_break) == 1:
        continue

      # TODO; right now, relying on exceptions for the error handling
      df_start_index = dow_full.index(second_break[0])
      df_end_index = dow_full.index(second_break[1])

      for f in dow_full[df_start_index:df_end_index]:
        dow_list.append(f)             
    
    return dow_list



def findFirst(pattern, text):
  find = re.findall(pattern, text)
  if not find or len(find) == 0:
    return None
  
  return find[0]

