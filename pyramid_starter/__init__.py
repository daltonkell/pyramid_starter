from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_starter.routes') # <-- include routes from routes.py
    config.scan()
    return config.make_wsgi_app()
