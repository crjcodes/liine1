from flask import Flask
import api_startup
import operating_hours_manager

# STARTUP

manager = operating_hours_manager.Manager()
api_startup.perform_startup_steps(manager)

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
