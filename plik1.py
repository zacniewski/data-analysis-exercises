with open("demofile.txt", "a+") as f:
    for i in range(10):
        zm = str(i) + "\n"
        f.write(zm)
