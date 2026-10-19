import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def greet(self):
        return f"こんにちは、{self.name}（{self.age}歳）です！"

# --- JSON から読み込んで Person を復元 ---
people = []

try:
    with open("persons.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for item in data:
            name = item["name"]
            age = item["age"]
            people.append(Person(name, age))

    print("Day29：JSON から Person を復元しました。\n")

    for p in people:
        print(p.greet())

except FileNotFoundError:
    print("persons.json が見つかりません。Day29（保存編）を先に実行してください。")
