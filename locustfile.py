import time
from locust import HttpUser, task, between
import json
class QuickstartUser(HttpUser):
    # requst content for house pricing project
    with open('request.json', 'r') as f:
        content_raw = f.read()
    content_json = json.loads(content_raw)
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/")
        self.client.post("/_dash-update-component", json=self.content_json)


    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)
    #
    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})
