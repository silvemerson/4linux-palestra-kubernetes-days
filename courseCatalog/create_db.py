from project import db,app
from sqlalchemy_utils.functions import database_exists,create_database,database_exists


if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
  create_database(app.config['SQLALCHEMY_DATABASE_URI'])

db.init_app(app)
db.create_all()
db.session.commit()
