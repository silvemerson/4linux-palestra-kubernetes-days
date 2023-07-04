import os
import unittest
from project import app,db
from project.models import Users


class AllTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def login(self, name, password):
        return self.app.post('/',data=dict(
            name=name,password=password), follow_redirects=True)

    def logout():
        return self.app.get('/logout',follow_redirects=True)

    def register(self,name,email,password,confirm):
        return self.app.post('/register',data=dict(
            name=name,email=email,password=password,confirm=confirm),
            follow_redirects=True)

    def test_user_can_register(self):
        new_user = Users('devops','devops@example.com','qwe123qwe','qwe123qwe')
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(Users).all()
        for row in test:
            assert row.name == 'devops'

    def test_user_can_loging(self):
        self.register('devops','devops@example.com','qwe123qwe','qwe123qwe')
        response = self.login('devops','qwe123qwe')
        self.assertIn(b'Bem vindo ao Painel de Cursos!!!', response.data)


if __name__ == '__main__':
    unittest.main()
