from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When i call #all
I get all the albums in the albums table
"""
def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "Graduation", 2007, 1)
    ]


"""
When i call #create
I create an album in the database and I can see it in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test Title', 2000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, "Graduation", 2007, 1),
        Album(2, 'Test Title', 2000, 2)
    ]