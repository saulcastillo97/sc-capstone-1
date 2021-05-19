import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, db, Movie, Actor
from sqlalchemy import exc
import requests ##

import json
import sys

from auth.auth import AuthError, requires_auth

##---------------------------------------------------------------
## App initialization (Create and Config)
##---------------------------------------------------------------
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST,DELETE, OPTIONS')

        return response

##---------------------------------------------------------------
## Homepage Endpoint
##---------------------------------------------------------------
    @app.route('/')
    def homepage():
        return 'Welcome to my Capstone. Thank you Udacity, for helping change my life!'

##---------------------------------------------------------------
## GET actor and movie Endpoints
##---------------------------------------------------------------

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            return jsonify ({
                'success': True,
                'actors':[actor.format() for actor in Actor.query.all()]
            }), 200
        except Exception as e:
            #print(payload)
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            return jsonify ({
                'success': True,
                'movies': [movie.format() for movie in Movie.query.all()]
            }), 200
        except:
        #expect Exception as e:
        #    print(e)\
            print(payload)
            abort(422)

##---------------------------------------------------------------
## DELETE actor and movie Endpoints
##---------------------------------------------------------------

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                'success':True,
                'actor':id
            }), 200
        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        if not id:
            abort(404)

        movie_to_remove = Movie.query.filter_by(id=id)
        if not movie_to_remove:
            abort(404)

        try:
            movie_to_remove.delete()
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

        return jsonify({
        'success': True,
        'id': id
        }), 200

    #@app.route('/movies/<int:id>', methods=['DELETE'])
    #@requires_auth('delete:movies')
    #def delete_movie(payload, id):
    #    movie = Movie.query.filter(Movie.id == id).one_or_none()
    #    movie.delete()
#
    #    if movie is None:
    #        abort(404)
#
    #    try:
    #        movie.delete()
#
    #        return jsonify({
    #            'success':True,
    #            'movie': [movie.format()]
    #        }), 200
    #    except Exception as e:
    #        print(e)
    #        abort(422)

##---------------------------------------------------------------
## POST actor and movie Endpoints
##---------------------------------------------------------------

    @app.route('/actors', methods=['GET', 'POST'])
    #@cross_origin()
    @requires_auth('post:actors')
    def post_actor(paylaod):
        try:
            data = request.get_json()
            new_actor = Actor(
                name = data.get('name', None),
                age = data.get('age', None),
                gender = data.get('gender', None)
            )
            new_actor.insert()

            print('Actor: ' + new_actor.name)
            selection = Actor.query.all()
            actors = []

            return jsonify({
                'success': True
                #'actor':[new_actor.format()]
            }), 200
        except Exception as e:
            #url = 'http://127.0.0.1:5000/actors'
            #x = request.get(url)
            #print(x.json())
            print(e)
            abort(422)

    @app.route('/movies', methods=['GET', 'POST'])
    #@cross_origin()
    @requires_auth('post:movies')
    def post_movie(payload):
        try:
            data = request.get_json()
            new_movie = Movie(
                title = data.get('title', None),
                release_date = data.get('release_date', None)
            )
            new_movie.insert()

            print('Movie: ' + new_movie.title)
            selection = Movie.query.all()
            movies = []

            return jsonify ({
                'success': True
                #'movie':[new_movie.format()]
            }), 200
        except Exception as e:
            print(e)
            abort(422)

##---------------------------------------------------------------
## PATCH actor and movie Endpoint Tests
##---------------------------------------------------------------
    #@app.route('/actors/<int:id>', methods=['PATCH'])
    #@requires_auth('patch:actors')
    #def update_actor(payload, id):
    #    try:
    #        actor = Actor.query.get(id)
    #        data = request.get_json()
#
    #        if 'name' in data:
    #            actor.name = json.dumps(data['title'])
    #        if 'age' in data:
    #            actor.age = json.dumps(data['age'])
    #        if 'gender' in data:
    #            actor.gender = json.dumps(data['gender'])
#
    #        actor.update()
#
    #        return jsonify({
    #            'success': True,
    #            'actor': [actor.format()]
    #        }), 200
    #    except Exception as e:
    #        print(e)
    #        print(data)
    #        abort(422)
    @app.route('/actors/<int:id>', methods=['GET', 'PATCH'])
    @requires_auth('patch:actors')
    def update_actor_form(payload, id):
        actor = Actor.query.get(id)

        if actor is None:
            return json.dumps({
                'success': False,
                'error': 'Actor could not be found to be updated',
            }), 404

        actor_details = ({
            "id": actor.id,
            "name": actor.name,
            "age": actor.age,
            "gender": actor.gender,
        })
        return jsonify(actor_details)
    ###@app.route('/actors/<int:id>', methods=['PATCH'])
    ###@requires_auth('patch:actors')
    ###def edit_actor(payload, id):
    ###    try:
    ###        updated_actor = request.get_json()
    ###        updated_name = updated_actor.get('name')
    ###        updated_age = updated_actor.get('age')
    ###        updated_gender = updated_actor.get('gender')
    ###        actor = Actor.query.filter_by(id=id).first()
    ###        if actor:
    ###            if updated_name:
    ###                actor.name = updated_name
    ###            if updated_birth_date:
    ###                actor.birth_date = updated_birth_date
    ###            if updated_gender:
    ###                actor.gender = updated_gender
    ###            actor.update()
    ###        else:
    ###            print(id)
    ###            abort(404)
    ###        return jsonify({
    ###            'success': True,
    ###            'actor': [actor.format()]
    ###        })
    ###    except Exception as e:
    ###        print(e)
    ###        abort(400)

    ##@app.route('/actors/<int:id>', methods=['PATCH'])
    ##@requires_auth('patch:actors')
    ##def update_actor(payload, id):
    ##    if not id:
    ##        abort(404)
##
    ##    actor = Actor.query.get(id)
##
    ##    if not actor:
    ##        abort(404)
##
    ##    data = request.get_json()
##
    ##    if 'name' in data and data['name'] != '':
    ##        actor.name = data['title']
    ##    if 'age' in data and data['age'] != '':
    ##        actor.age = data['age']
    ##    if 'gender' in data and data['gender'] != '':
    ##        actor.gender = data['gender']
##
    ##    actor.update()
##
    ##    return jsonify({
    ##        'success': True,
    ##        'actor': actor.format()
    ##    }), 200

#####        print(data)

    #@app.route('/movies/<int:id>', methods=['PATCH'])
    #@requires_auth('patch:movies')
    #def update_movie(payload, id):
    #    movie = Movie.query.get(id)
    #    if movie is None:
    #        abort(404)
#
    #    data = request.get_json()
    #    if 'title' in data:
    #        movie.title = json.dumps(data['title'])
    #    if 'release_date' in data:
    #        movie.title = json.dumps(data['release_date'])
    #    movie.update()
    #    return jsonify({
    #        'success': True,
    #        'movie': [movie.format()]
    #    }), 200
######
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):
        if not id:
            abort(404)

        movie = Movie.query.get_or_404(id)
        if not movie:
            abort(404)

        data = request.get_json()

        if 'title' in data and data['title'] != '':
            movie.title = data['title']

        if 'release_date' in data and data['release_date'] != '':
            movie.release_date = data['release_date']

        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.format(),
        }), 200


######
    #@app.route('/movies/<int:id>', methods=['PATCH'])
    #@requires_auth('patch:movies')
    #def update_movie(payload, id):
    #  error = False
    #  data = {}
    #  try:
    #      data = request.get_json()
    #      title = data['title']
    #      release_date = data['release_date']
#
    #      movie = Movie(title=title, release_date=release_date)
    #      movie.insert()
#
    #  except():
    #      error = True
     # if error:
    #      abort(500)
    #  else:
    #      moviesarray = []
    #      moviesarray.append(movie.format())
    #      return jsonify ({
    #        'success': True,
    #        'movie': moviessarray
    #        })


        #try:
        #    updated_movie = request.get_json()
        #    updated_title = updated_movie.get('title')
        #    updated_release_date = updated_movie.get('release_date')
        #    movie = Movie.query.filer_by(id==id).first()
        #if movie:
        #    if updated_title:
        #        movie.title = updated_title
        #    if updated_release_date:
        #        movie.release_date = updated_release_date
        #    movie.update()
        #else:
        #    abort(404)
        #return jsonify({
        #    'success': True,
        #    'movie':
        #})
    #expect Exception as e:
        #print(e)
        #abort(400)

##---------------------------------------------------------------
## Error Handlers (400, 401, 403, 404, 422, 500 and AuthError)
##---------------------------------------------------------------

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden request"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success":False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success":False,
            "error": 500,
            "message": "something went wrong"
        }), 500

    @app.errorhandler(AuthError)
    def autherror(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #APP.run(host='0.0.0.0', port=8080, debug=True)
