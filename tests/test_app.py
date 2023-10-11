# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /sort-names
And: I send a list of names as the body parameter text
Then: I should get a 200 response 
      I should also get a sorted list of names sepreated with commas
"""
def test_post_list_of_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a POST request to /sort-names
And: I send a list of names as the body parameter text
Then: I should get a 200 response 
      I should also get a sorted list of names sepreated with commas
"""
def test_post_list_of_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Aaab,Aaaz,Aaac'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaab,Aaac,Aaaz'


"""
When: I make a GET request to /names
And: Return list of pre-defined names plus given names
Then: I should get a 200 response 
"""
def test_get_list_of_names_plus_given_name(web_client):
    response = web_client.get('/names?add=Eddie', data={'names': 'Julia, Alice, Karim'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'



def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'My Beautiful Dark Twisted Fantasy',
        'release_year': '2010',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    
    expected_response = "Album 1(1, Graduation, 2007, 1)\n" \
                       "Album 2(2, My Beautiful Dark Twisted Fantasy, 2010, 1)"
    assert get_response.data.decode('utf-8') == expected_response

