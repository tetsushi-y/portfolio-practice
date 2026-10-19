class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"こんにちは、{self.name}（{self.age}歳）です！"

# --- 複数インスタンスを作成 ---
people = [
    Person("哲志", 48),
    Person("太郎", 30),
    Person("花子", 25)
]

# --- 全員の自己紹介を表示 ---
print("Day26：複数の Person を管理するアプリ\n")

for p in people:
    print(p.greet())
