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
_____________

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

#### GET /movies
#### DELETE /actors/int:id
#### DELETE /actors/int:id
#### POST /actors
#### POST /movies
#### PATCH /actors/int:id
``` python
payload = {
  name: Mark Hamill
  age: 69
  gender: male
}
```
#### PATCH /movies/int:id
``` python
{
  title: The Empire Strikes Back,
  release_date: 05,21,1980
}
```

## Testing
To run unittests for this application run:

``` python
python test_app.py
```
