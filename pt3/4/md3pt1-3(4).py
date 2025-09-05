import json


def register():
    login = input('login: ').strip()
    password = input('password: ').strip()
    return login, password
login, password = register()
auth = {
        'username':login,
        'passwd':password
}
with open('auth.json', 'w', encoding='utf-8') as file:
    json.dump(auth, file)

print(auth)
