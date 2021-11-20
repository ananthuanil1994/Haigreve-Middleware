from src import app
from src.routes.routes import teletalk_routes
from config import APP_DEBUG


app.register_blueprint(teletalk_routes)

if __name__ == '__main__':
    # start_scheduler()
    # app.run(debug=True, use_reloader=False)
    app.run(debug=APP_DEBUG)
