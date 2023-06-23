
############## see beginning of video 33 ##################

# Import the dependencies.
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from flask import Flask, jsonify
import json

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"""<h1>Available Routes:</h1><br/>"""
        f"""/api/v1.0/precipitation<br/>"""
        f"""/api/v1.0/passengers"""

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Get precipitation"""
    query = text("""
                SELECT
                    date,
                    station,
                    prcp
                FROM
                    measurement
                WHERE
                    date > '2016-08-22';
            """)

    df = pd.read_sql(query, engine)

    # convert to JSON
    data = json.loads(df.to_json(orient="records"))
    return(data)


if __name__ == '__main__':
    app.run(debug=True)
















