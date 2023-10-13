import os
from flask import Flask, request
from lib.album import Album
from lib.album_repository import AlbumRepository

from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/submit', methods=['POST'])
def post_submit():
    # Get the values of 'name' and 'message' from the request's form data
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    # Get the value of 'name' from the request's form data
    name = request.form['name']
    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    # Get the value of 'name' from the request's form data
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'

@app.route('/sort_names', methods=['POST'])
def post_list_of_names():
    # Get the value of 'names' from the request's form data
    names = request.form['names'].split(',')
    sort_names = sorted(names)
    return ','.join(sort_names)

# Initialize the list of names
names_list = ['Julia', 'Alice', 'Karim']

@app.route('/names', methods=['GET'])
def get_list_of_names_plus_given_name():
    added_name = request.args.get('add')
    
    if added_name:
        names_list.append(added_name)  # Append the added_name to the names_list

    return ', '.join(names_list)  # Return the updated names list as a comma-separated string

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '', 200

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()

    # Convert Album objects to their string representations
    album_strings = [f"Album {album.id}({album.id}, {album.title}, {album.release_year}, {album.artist_id})" for album in albums]

    return "\n".join(album_strings)



# Sample list of artists
artists = ["Pixies", "ABBA", "Taylor Swift", "Nina Simone"]

@app.route('/artists', methods=['GET'])
def get_artists():
    return ', '.join(artists), 200

@app.route('/artists', methods=['POST'])
def create_artist():
    data = request.form
    name = data.get('name')
    genre = data.get('genre')

    if name and genre:
        artists.append(name)
        return '', 200
    else:
        return 'Invalid request', 400



    

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




