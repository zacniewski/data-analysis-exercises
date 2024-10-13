import requests

users_url = "http://jsonplaceholder.typicode.com/users"
all_users = requests.get(users_url).json()

with open("users.txt", "a+") as f:
    for item in all_users:
        id = item["id"]
        name = item["name"]
        city = item["address"]["city"]
        longitude = item["address"]["geo"]["lng"]

        linia_do_zapisu = f"{id}. {name} from {city} (longitude: {longitude}).\n"
        f.write(linia_do_zapisu)
