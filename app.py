import requests
endpoint = requests.get("https://dog.ceo/api/breeds/image/random")
if endpoint.json()["status"] == "success":
    print(f"{endpoint.json()["message"]}")