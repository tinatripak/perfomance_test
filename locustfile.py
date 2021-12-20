from locust import HttpUser, task, between


class User(HttpUser):
    time = between(1, 5)
    host = 'https://reqres.in/api'

    @task(1)
    def list_users(self):
        self.client.get("/users")

    @task(3)
    def create_oneuser(self):
        self.client.post("/users", json={
            "name": "Kristina Tripak",
            "job": "UI/UX Designer"
        })

    @task(3)
    def update_user(self):
        self.client.put("/users", json={
            "name": "Kristina",
            "surname": "Tripak"
        })

    @task(1)
    def delete_user(self):
        self.client.delete("/users/2")

    @task(1)
    def log_user(self):
        self.client.get("/user/login", json={
            "username": "login123",
            "password": "qwertyqwerty"
        })

    @task(1)
    def logout_user(self):
        self.client.get("/user/logout")
