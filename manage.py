from server_app.extensions import Flask, Manager, pywsgi
from server_app.add_api import add_api

app = Flask(__name__)

add_api(app)

manager = Manager(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@manager.shell
def make_shell_context():
    return dict(
        app=app,
    )


@manager.command
def pro_run():
    print('listening for request')
    gevent_server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    gevent_server.serve_forever()


@manager.command
def dev_run():
    print('dev_run')
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
    app.config(**config)
    app.run()


if __name__ == '__main__':
    manager.run()
