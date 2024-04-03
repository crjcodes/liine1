from flask import Flask
from operating_hours_manager import OperatingHoursManager

OpHoursManager = OperatingHoursManager()

# TODO: parsing of the csv into the json data format on startup
# ParsingManager -> Accessor

app = Flask(__name__)

@app.route("/")
@app.route('/restaurants/open')

def handle_restaurants_open():
  return OpHoursManager.list_operating_restaurants()

if __name__ == "__main__":
  app.run(debug=True)