from flask import Flask
import operating_hours_manager

# STARTUP

try:
  manager = operating_hours_manager.Manager()

  # TODO: FUTURE: name of file input through command-line and configuration
  # TODO: figure out how to reference the file in a data directory, not just source
  manager.ingest_new_data_source("restaurants.csv")
except Exception as err:
    print(f"Startup failure due to unexpected {err=}, {type(err)=}")
    raise

# ROUTE SETUP

try: 
  app = Flask(__name__)

  @app.route("/")
  @app.route('/restaurants/open')

  def handle_restaurants_open():
    return manager.list_operating_restaurants()
   
except Exception as err:
    print(f"Endpoint route setup failure due to unexpected {err=}, {type(err)=}")
    raise 

if __name__ == "__main__":
  app.run(debug=True)
