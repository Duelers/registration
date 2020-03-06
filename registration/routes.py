from views import signup


def setup_routes(app):
    app.router.add_post('/public/v1/signup/', signup)
