import json
import os

class Model:
    def save(self, filename="database.json"):
        data = {key: value for key, value in self.__dict__.items() if not key.startswith("_")}

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = []
        else:
            all_data = []

        all_data.append(data)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)

        print(f"{self.__class__.__name__} сохранён в {filename}")


class Post(Model):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


post1 = Post("Заголовок первой статьи", "Содержание первой статьи", "Артём")
post1.save()

post2 = Post("Заголовок второй статьи", "Содержание второй статьи", "Артём")
post2.save()