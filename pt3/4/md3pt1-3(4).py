import json

def register():
    login = input('login: ').strip()
    password = input('password: ').strip()
    return login, password
def login_function(auth):
    while True:
        login = input('login: ').strip()
        password = input('password: ').strip()
        if login in auth and auth[login] == password:
             print("вы молодец, помните свои учетные данные")
             break
        else:
            print("wrong")
try:
    with open('auth.json', 'r', encoding='utf-8') as f:
        auth = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    auth = {}


choice = input('регистрация или вход? ').strip().lower()

if choice == 'регистрация':
    while True:
        login, password = register()
        if login in auth:
            print("change name")
        else:
            auth[login] = password
            with open('auth.json', 'w', encoding='utf-8') as file:
                json.dump(auth, file)
            print("login add")
            break
else:
    login_function(auth)
print(auth)