from crud import create_item, delete_item, get_item, patch_item
from models import User, Adv, get_session_maker

from flask import jsonify, request
from flask.views import MethodView


Session = get_session_maker()


def _get_json(obj, model):
    if model == 'User':
        objects = {
            'id': obj.id,
            'email': obj.email,
            'registration_time': obj.registration_time.isoformat()
        }
    elif model == 'Adv':
        objects = {
            'title': obj.title,
            'description': obj.description,
            'creation_time': obj.creation_time.isoformat(),
            'owner': obj.owner
        }
    else:
        objects = {}

    return jsonify(objects)


class UserView(MethodView):
    def get(self, user_id: int):
        with Session() as session:
            user = get_item(session, User, user_id)

            return _get_json(user, 'User')

    def post(self):
        with Session() as session:
            data = request.json
            user = create_item(session, User, **data)

            return _get_json(user, 'User')

    def patch(self, user_id: int):
        with Session() as session:
            data = request.json
            user = get_item(session, User, user_id)
            user = patch_item(session, user, **data)

            return _get_json(user, 'User')

    def delete(self, user_id: int):
        with Session() as session:
            user = get_item(session, User, user_id)
            delete_item(session, user)

            return {'deleted': True}


class AdvView(MethodView):
    def get(self, adv_id: int):
        with Session() as session:
            adv = get_item(session, Adv, adv_id)

            return _get_json(adv, 'Adv')

    def post(self):
        with Session() as session:
            data = request.json
            adv = create_item(session, Adv, **data)

            return _get_json(adv, 'Adv')

    def patch(self, adv_id: int):
        with Session() as session:
            data = request.json
            adv = get_item(session, Adv, adv_id)
            adv = patch_item(session, adv, **data)

            return _get_json(adv, 'Adv')

    def delete(self, adv_id: int):
        with Session() as session:
            adv = get_item(session, Adv, adv_id)
            delete_item(session, adv)

            return {'deleted': True}
