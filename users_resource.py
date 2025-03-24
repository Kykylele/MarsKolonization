from flask_restful import Resource, reqparse

from data import users
from data.db_session import create_session
from data.users import User
from flask import jsonify, abort


parser = reqparse.RequestParser()
parser.add_argument('surname', required=False)
parser.add_argument('name', reqired=False)
parser.add_argument('age', required=False, type=int)
parser.add_argument('position', reqired=False)
parser.add_argument('speciality', required=False)
parser.add_argument('address', reqired=False)
parser.add_argument('email', required=False)
parser.add_argument('hashed_password', reqired=False)


class UsersResource(Resource):
    def get(self, us_id):
        sess = create_session()
        user = sess.query(User).filter(User.id == us_id).first()
        if not user:
            abort(404, 'Not found')
        return jsonify(user.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address',
                                          'email', 'hashed_password', 'modified_date')))

    def delete(self, us_id):
        sess = create_session()
        user = sess.query(User).filter(User.id == us_id).first()
        if not user:
            abort(404, 'Not found')
        sess.delete(user)
        sess.commit()
        return jsonify({'status': 'ok'})


class UsersListResource:
    def get(self):
        sess = create_session()
        user = sess.query(User).all()
        if not user:
            abort(404, 'Not found')
        return jsonify([user.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address',
                                          'email', 'hashed_password', 'modified_date')) for user in users])

    def post(self):
        args = parser.parse_args()
        sess = create_session()
        user = User(surname=args['surname'],
                    name=args['name'],
                    age=args['age'],
                    position=args['position'],
                    speciality=args['speciality'],
                    address=args['address'],
                    email=args['email'],
                    hashed_password=args['hashed_password'])
        sess.add(user)
        sess.commit()
        return jsonify({'user_id': user.id})
