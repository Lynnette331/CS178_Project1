

from flask import Flask, render_template, request, redirect # type: ignore
import pymysql # type: ignore
import boto3
import os
import creds
from creds import host, user, password, db

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

app = Flask(__name__)

@app.route('/')
def index():
    connection = None
    try:
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        #query to fetch movies with genres
        genres_query = """
        SELECT movie.movie_id AS id, movie.title, movie.budget, genre.genre_name AS genre_name
        FROM movie
        JOIN movie_genres ON movie.movie_id = movie_genres.movie_id
        JOIN genre ON movie_genres.genre_id = genre.genre_id
        LIMIT 15;
        """
        cursor.execute(genres_query)
        genres_results = cursor.fetchall()
        return render_template('index.html', results=genres_results)  # Rendering the template
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()

#route to fetch all movies
@app.route('/add_movie', methods=['POST'])
def add_movie():
    connection = None
    try:
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        # Get movie details from the form
        title = request.form['title']
        budget = request.form['budget']
        movie_id = request.form['movie_id']
        # Insert the new movie into the database
        cursor.execute("INSERT INTO movie (title, budget, movie_id) VALUES (%s, %s, %s)", (title, budget, movie_id))
        connection.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()

#route to update movie details
@app.route('/update_movie', methods=['POST'])
def update_movie():
    connection = None
    try:
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        # Get updated details from the form
        movie_id = request.form['movie_id']
        title = request.form['title']
        budget = request.form['budget']
        # Update the movie in the database
        cursor.execute("UPDATE movie SET title = %s, budget = %s WHERE movie_id = %s", (title, budget, movie_id))
        connection.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()

#route to delete a movie
@app.route('/delete_movie', methods=['POST'])
def delete_movie():
    connection = None
    try:
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        # Get the movie ID from the form
        movie_id = request.form['movie_id']
        # Delete the movie from the database
        cursor.execute("DELETE FROM movie WHERE movie_id = %s", (movie_id,))
        connection.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()

    
#route to fetch the table of movies with genres
@app.route('/movies_with_genres')
def movies_with_genres():
    connection = None
    try:
        connection = pymysql.connect(
            host=creds.host,
            user=creds.user,
            password=creds.password,
            database=creds.db
        )
        cursor = connection.cursor()
        query = """
        SELECT movie.movie_id AS id, movie.title, movie.budget, genre.genre_name AS genre_name
        FROM movie
        JOIN movie_genres ON movie.movie_id = movie_genres.movie_id
        JOIN genre ON movie_genres.genre_id = genre.genre_id
        LIMIT 15;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('movies_with_genres.html', results=results)
    except Exception as e:
        return f"Error: {e}"
    finally:
        if connection:
            connection.close()



if __name__ == '__main__':
    app.run(debug=True)