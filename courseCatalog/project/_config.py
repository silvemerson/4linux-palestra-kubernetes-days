WTF_CSRF_ENABLED = True
SECRET_KEY = b'emeW7Bb48Wai6SIiVIorvn+SsHM='

DATABASE = "simplePythonFlask"
#SQLALCHEMY_DATABASE_URI = 'mysql://root:qwe123qwe@127.0.0.1:3306/'+DATABASE
SQLALCHEMY_DATABASE_URI = 'mysql://root:qwe123qwe@mariadb.web.svc.cluster.local:3306/'+DATABASE
# SQLALCHEMY_DATABASE_URI = 'mysql://root:qwe123qwe@mariadb:3306/'+DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = False
