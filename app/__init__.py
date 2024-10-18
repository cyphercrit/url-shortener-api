from app.config import Config, Database
from app.routes import URLRoutes

app = Config().init_app()
db = Database(app).get_db()
app.register_blueprint(URLRoutes().routes)