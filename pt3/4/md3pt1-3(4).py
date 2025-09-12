import json
from pathlib import Path


AUTH_FILE = Path("auth.json")


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
    choice = input("Регистрация или вход? ").strip().lower()

    if choice == "регистрация":
        register(auth)
    else:
        login_function(auth)

    print("Текущая база пользователей:", auth)


if __name__ == "__main__":
    main()
