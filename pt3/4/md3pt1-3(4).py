def register(username, password, filename="users.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            names = {line.split(":",1)[0].strip() for line in f}
    except FileNotFoundError:
        names = set()
    if username in names:
        return False
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{username}:{password}\n")
    return True


def login_function(username, password, filename="users.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                saved_username, saved_password = line.strip().split(":", 1)
                if saved_username == username and saved_password == password:
                    return True
    except FileNotFoundError:
        return False
    return False
