class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"こんにちは、{self.name}（{self.age}歳）です！"

# --- ここから実行部分 ---
p = Person("哲志", 48)
print(p.greet())
