from unittest import TestCase
from fastapi.testclient import TestClient
from app import app
from app.models import Base
from app.database import engine


client = TestClient(app)



class TestRoom(TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def test_correct_create_acc(self):

        data = {"firebase_id": "this_is_id"}
        response = client.post("/api/users", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("firebase_id", response.json())
        self.assertIn("user_id", response.json())
        self.assertEqual("this_is_id", response.json()["firebase_id"])
        self.assert

    def test_incorrect_create_acc(self):
        data = {}
        response = client.post("/api/users", json=data)
        self.assertEqual(response.status_code, 422)

    def test_not_unique_create_acc(self):
        data = {"firebase_id": "this_is_id123"}
        response = client.post("/api/users", json=data)
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/users", json=data)
        self.assertEqual(response.status_code, 409)




