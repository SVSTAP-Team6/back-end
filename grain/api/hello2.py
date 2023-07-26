from grain.blueprints import hello_test


@hello_test.route('/say')
def say_hello_world():
    return 'Hello World!'
