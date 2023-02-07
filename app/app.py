import atexit

from flask import Flask

from models import close_db, init_db
from errors import ApiError, error_handler
from views import AdvView, UserView


init_db()
atexit.register(close_db)

app = Flask('app')

user_view = UserView.as_view('user_view')
adv_view = AdvView.as_view('adv_view')

app.add_url_rule('/user/<int:user_id>', view_func=user_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/user', view_func=user_view, methods=['POST'])
app.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/adv', view_func=adv_view, methods=['POST'])

app.errorhandler(ApiError)(error_handler)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
