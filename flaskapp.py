

from flask import Flask, render_template # type: ignore
import pymysql # type: ignore
import creds
from creds import host, user, password, db

print("Flask app is starting...")

app = Flask(__name__)

@app.route('/')
def index():
    connection = None
    try:
        # Connect to the RDS MySQL database
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        # Query to fetch movies
        cursor.execute("SELECT title, budget, movie_id FROM movie LIMIT 10;")
        results = cursor.fetchall()
        return render_template('index.html', results=results)
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)