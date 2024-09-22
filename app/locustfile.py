from locust import HttpUser, task
from random import randint


class SampleLocustTest(HttpUser):
    @task(30)
    def list_students(self):
        self.client.get("/students/")

    @task(70)
    def get_student(self):
        _rand_registration = randint(50, 60)
        self.client.get(f"/students/?registration={_rand_registration}")
