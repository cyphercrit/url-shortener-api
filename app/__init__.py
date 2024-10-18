from app.config import Config, Database

config = Config()
app = config.init_app()

database = Database(app)
db = database.get_db()

from app.routes import routes
app.register_blueprint(routes)