import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

# --- 複数インスタンスを作成 ---
people = [
    Person("哲志", 48),
    Person("太郎", 30),
    Person("花子", 25)
]

# --- JSON に保存 ---
data = [p.to_dict() for p in people]

with open("persons.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Day29：Person データを persons.json に保存しました。")
