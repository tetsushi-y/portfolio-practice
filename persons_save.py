import csv

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_row(self):
        return [self.name, self.age]

# --- 複数インスタンスを作成 ---
people = [
    Person("哲志", 48),
    Person("太郎", 30),
    Person("花子", 25)
]

# --- CSV に保存 ---
with open("persons.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["名前", "年齢"])  # ヘッダー
    for p in people:
        writer.writerow(p.to_row())

print("Day27：Person データを persons.csv に保存しました。")
