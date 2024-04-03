from flask import Flask
from operating_hours_manager import *

# TODO: parsing of the csv into the json data format on startup
# ParsingManager -> Accessor

app = Flask(__name__)

@app.route("/")
@app.route('/restaurants/open')

# TODO: route to a HoursOfOperationManager.ListOpenRestaurants({datetime})

def handle_restaurants_open():

  return list_operating_restaurants()

if __name__ == "__main__":
  app.run(debug=True)