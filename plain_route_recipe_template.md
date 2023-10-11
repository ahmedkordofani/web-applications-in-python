# {{ NAME }} Route Design Recipe

Test-drive a route POST /albums to create a new album:


Here's a description of the expected behaviour:
```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)
```
## 1. Design the Route Signature

POST /albums
  title: string
  release_year: number(str)
  artist_id: number(str)

GET /albums


## 2. Create Examples as Tests


```python
# Scenario 1

# POST /albums
# title: "My Beautiful Dark Twisted Fantasy"
# release_year: "2010"
# artist_id: 1
#  Expected response (200 OK):
"""
no content
"""

# GET /albums
#  Expected response (200 OK):
"""
Album 1(1, Graduation, 2007, 1)
Album 2(2, My Beautiful Dark Twisted Fantasy, 2010, 1)
"""


# Scenario 2

# POST /albums
#  Expected response (400 OK):
"""
no content
"""

# GET /albums
#  Expected response (200 OK):
"""
Album 1(1, Graduation, 2007, 1)
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
