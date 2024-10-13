import requests

comments_url = "http://jsonplaceholder.typicode.com/comments"
all_comments = requests.get(comments_url).json()

with open("emails.txt", "a+") as f:
    for comment in all_comments:
        id = comment["id"]
        email = comment["email"]
        linia_do_zapisu = f"{id}. {email}\n"
        f.write(linia_do_zapisu)
