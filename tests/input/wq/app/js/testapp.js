requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'testapp': '../testapp',
        'data': '../data/'
    }
});

requirejs(['testapp/main']);
