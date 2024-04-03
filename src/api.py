from flask import Flask
import operating_hours_manager

manager = operating_hours_manager.manager()

# TODO: parsing of the csv into the json data format on startup
manager.ingest_new_data_source("my.csv")

app = Flask(__name__)

@app.route("/")
@app.route('/restaurants/open')

def handle_restaurants_open():
  return manager.list_operating_restaurants()

if __name__ == "__main__":
  app.run(debug=True)