from flask import Blueprint


def _factory(partial_module_string, url_prefix):
    name = partial_module_string
    import_name = 'grain.api.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    return blueprint


hello = _factory('hello', '/hello_world')
hello_test = _factory('hello2', '/hello_world2')

all_blueprints = (hello, hello_test)
