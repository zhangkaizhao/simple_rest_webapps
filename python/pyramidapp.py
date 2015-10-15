from pyramid.view import view_defaults
from pyramid.response import Response
from pyramid.config import Configurator


@view_defaults(route_name='rest')
class RESTView(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        return Response('Hello, world!')


def main(global_config, **settings):
    config = Configurator()
    config.add_route('rest', '/')
    config.add_view(RESTView, attr='get', request_method='GET')
    return config.make_wsgi_app()


application = main({})


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    try:
        print('Visit http://localhost:8080/')
        make_server('', 8080, application).serve_forever()
    except KeyboardInterrupt:
        pass
    print('\nThanks!')
