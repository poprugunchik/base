import json
from pathlib import Path


AUTH_FILE = Path("auth.json")
USER_NAME = "testuser"
USER_PASSWORD = "1234"

def load_auth():
    if AUTH_FILE.exists():
        try:
            with open(AUTH_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_auth(auth):
    with open(AUTH_FILE, "w", encoding="utf-8") as f:
        json.dump(auth, f, ensure_ascii=False, indent=4)


def get_credentials():
    choice = input("Загрузить или ввести? ").strip().lower()

    if choice == "загрузить":
        login = USER_NAME
        password = USER_PASSWORD
    else:
        login = input("Логин: ").strip()
        password = input("Пароль: ").strip()
    return login, password


def register(auth):
    while True:
        login, password = get_credentials()
        if login in auth:
            print("Такой логин уже существует, попробуйте другой.")
        else:
            auth[login] = password
            save_auth(auth)
            print("Регистрация успешна!")
            break


def login_function(auth):
    while True:
        login, password = get_credentials()
        if auth.get(login) == password:
            print("Добро пожаловать!")
            break
        else:
            print("Неверный логин или пароль, попробуйте снова.")


def main():
    auth = load_auth()

    login, password = get_credentials()

    if login in auth:
        if auth[login] == password:
            print("Добро пожаловать!")
        else:
            print("Неверный пароль")
    else:
        auth[login] = password
        save_auth(auth)
        print("Регистрация успешна!")

    print("Текущая база пользователей:", auth)


if __name__ == "__main__":
    main()
