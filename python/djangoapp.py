from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG = True,
        INSTALLED_APPS = [],
        MIDDLEWARE_CLASSES = [],
        ROOT_URLCONF = 'djangoapp',
        TEMPLATE_DIRS = ['.'],
        DATABASES = {},
    )

from django.conf.urls import patterns
urlpatterns = patterns('',
    (r'^$', 'djangoapp.index'),
)

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world!')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#### Running

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()
