import requests

todos_url = "http://jsonplaceholder.typicode.com/todos"
all_todos = requests.get(todos_url).json()

counter = 0

with open("todos.txt", "a+") as f:
    for item in all_todos:
        id = item["id"]
        title = item["title"]
        completed = item["completed"]

        if completed:
            counter += 1
            linia_do_zapisu = f"Wpis o id={id} ma tytuł '{title}', a jego status to {completed}.\n"
            f.write(linia_do_zapisu)

    # f.seek(0)
    f.write(f"Liczba elementów ze statusem 'True' to {counter}.")
