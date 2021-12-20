from locust import HttpUser, task, between


class User(HttpUser):
    time = between(1, 5)
    host = 'https://reqres.in/api'

    @task(1)
    def list_users(self):
        self.client.get("/users")

    @task(3)
    def create_singleuser(self):
        self.client.post("/users", json={
            "name": "Kristina Tripak",
            "job": "UI/UX Designer"
        })

    @task(1)
    def create_user(self):
        self.client.post("/users", json={
            "name": "Kristina",
            "surname": "Tripak"
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
    def register_user(self):
        self.client.post("/register", json={
            "email": "emma.wong@reqres.in",
            "password": "pistol"
        })

    @task(1)
    def log_user(self):
        self.client.post("/login", json={
            "email": "emma.wong@reqres.in",
            "password": "pistol"
        })
