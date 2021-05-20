# scUdacityCapstone

## Motivation for project
I completed this project as the final project and capstone of Udacity's Nanodegrees program. I am thankful for all the help and guidance Udacity has given me. I am excited for what's to come and for the carreer change I am now posied to make.

## Dependencies
All of this project's dependencies are listed in the requirements.txt file. They can be installed by running: 
``` python
bash pip install -r requirements.txt 
```

## Running Server
First run:
``` python
export FLASK_APP.app.py;
```
Then run:
``` python
flask run --reload
```

## Heroku URL
https://sc-capstone-1.herokuapp.com/ | https://git.heroku.com/sc-capstone-1.git

## API Reference
### Error Handling
Errors are returned as JSON objects in the following format:
``` python
{
  'success': False,
  'message': 400
}
```
The API will return six error types when requests fail:
<ol>
  <li>400: bad request</li>
  <li>401: not found</li>
  <li>403: forbidden request</li>
  <li>404: resource not found</li>
  <li>422: unprocessable</li>
  <li>500: something went wrong</li>
 </ol>

### Roles and Permissions
<ul>
  <li>Casting Assistant
    <ul>PERMISSIONS
      <li>get:actors</li>
      <li>get:movies</li>
    </ul>
  </li>
  <li>Casting Director
    <ul>PERMISSIONS
      <li>get:actors</li>
      <li>get:movies</li>
      <li>delete:actors</li>
      <li>post:actors</li>
      <li>patch:actors</li>
      <li>patch:movies</li>
    </ul>
  </li>
  <li>Executive Producer
    <ul>PERMISSIONS
      <li>get:actors</li>
      <li>get:movies</li>
      <li>delete:actors</li>
      <li>delete:movies</li>
      <li>post:actors</li>
      <li>post:movies</li>
      <li>patch:actors</li>
      <li>patch:movies</li>
    </ul>
  </li>
</ul>

### Endpoints
#### GET /actors
- Gets list of actors
- Returns: An object with a success key and a list of actors.
``` python
{
    'success': True,
    'actors': [{
                'id': 1,
                'name': Saul,
                'age': 63,
                'gender': Male
               },
	       {
                'id': 2,
                'name': Brad,
                'age': 29,
              }]
}
```
#### GET /movies
- Gets list of movies
- Returns: An object with a success key and a list of movies.
``` python
{
    'success': True,
    'movies': [{
                'id': 1,
                'title': Test,
                'release_date': 2001-12-19,
               },
	       {
                'id': 1,
                'title': Test,
                'release_date': 2000-10-20,
               }]
}
```

#### DELETE /actors/int:id
- Deletes the actor with id: id
- Returns: Object with a success key and a list which contains the deleted actor id.
``` python
{
    'success': True,
    'actor': id
}
```
#### DELETE /movies/int:id
- Deletes the movie with id: id
- Returns: Object with a success key and a list which contains the deleted movie id.
``` python
{
    'success': True,
    'id': id
}
```
#### POST /actors
- adds an actor to the database
- Returns: An object with a success key
``` python
{
    'success': True,
}
```

#### POST /movies
- adds a movie to the database
- Returns: An object with a success key
``` python
{
    'success': True,
}
```

#### PATCH /actors/int:id
- updates the actor with id: id
- Returns: Object a list that contains the updated actor object.
``` python
{
    'success': True,
    'actor_details': [{
                'id': 1,
                'name': Saul,
                'age': 1900-10-12,
                'gender': Male
               }]
}
```
#### PATCH /movies/int:id
- updates the movie with id: id
- Returns: Object with a success key and a list which contains the updated movie object.
``` python
{
    'success': True,
    'movies': [{
                'id': 1,
                'title': Coco,
                'release_date': 2017-11-22,
               }]
}

```

## Testing
To run unittests for this application run:

``` python
python test_app.py
```
