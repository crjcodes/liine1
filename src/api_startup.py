import operating_hours_manager

def perform_startup_steps(manager, filename="restaurant.csv"):
  try:

    # TODO: FUTURE: name of file input through command-line and configuration
    # TODO: figure out how to reference the file in a data directory, not just source
    manager.ingest_new_data_source(filename)
  except Exception as err:
    print(f"Startup failure due to unexpected {err=}, {type(err)=}")
    raise  