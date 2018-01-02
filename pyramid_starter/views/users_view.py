from pyramid.view import view_config

@view_config(route_name='users', renderer='templates/mytemplate.jinja2')
def my_view(request):
    """
    Creates a view for the users table page.
    """
    return {'project': 'pyramid_starter'} # return the home page for now
