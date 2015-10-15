from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


class HelloView(MethodView):

    def get(self):
        return b'Hello, world!'


app.add_url_rule('/', view_func=HelloView.as_view('hello'))

application = app


if __name__ == "__main__":
    app.run()
