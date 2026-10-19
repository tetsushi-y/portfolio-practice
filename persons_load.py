import csv

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def greet(self):
        return f"こんにちは、{self.name}（{self.age}歳）です！"

# --- CSV から読み込んで Person を復元 ---
people = []

try:
    with open("persons.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダーをスキップ

        for row in reader:
            name, age = row
            people.append(Person(name, age))

    print("Day28：CSV から Person を復元しました。\n")

    for p in people:
        print(p.greet())

except FileNotFoundError:
    print("persons.csv が見つかりません。Day27 を先に実行してください。")
