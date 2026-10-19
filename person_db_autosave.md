# Python ミニアプリ（Day36）PersonDB 自動保存（Auto-Save）機能

## 🧮 概要
PersonDB に自動保存（auto-save）機能を追加し、
追加・削除・更新のたびにデータベースが自動的に保存されるようにしました。
AIエージェントの「永続化メモリ」の基礎となる重要なステップです。

## 🛠 使用技術
- Python
- VS Code
- クラス（Person / PersonDB）
- JSON 保存・読み込み
- 対話ループ（while True）
- ユーザー入力（input）
- 自動保存（auto-save）

## 📄 コード
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def to_dict(self):
        return {"name": self.name, "age": self.age}

    def greet(self):
        return f"こんにちは、{self.name}（{self.age}歳）です！"


class PersonDB:
    def __init__(self, filename="person_db.json"):
        self.filename = filename
        self.people = []

    def add(self, person):
        self.people.append(person)
        self.save()  # 自動保存

    def save(self):
        data = [p.to_dict() for p in self.people]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("（自動保存）データベースを保存しました。\n")

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.people = [Person(item["name"], item["age"]) for item in data]
            print("データベースを読み込みました。\n")
        except FileNotFoundError:
            print("データベースファイルがありません。新規作成します。\n")

    def find(self, name):
        for p in self.people:
            if p.name == name:
                return p
        return None

    def delete(self, name):
        for p in self.people:
            if p.name == name:
                self.people.remove(p)
                self.save()  # 自動保存
                return True
        return False

    def update(self, name, new_name, new_age):
        person = self.find(name)
        if person:
            person.name = new_name
            person.age = int(new_age)
            self.save()  # 自動保存
            return True
        return False


# --- メニュー操作 ---
db = PersonDB()
db.load()

while True:
    print("=== PersonDB メニュー（自動保存版） ===")
    print("1. 人を追加")
    print("2. 全員を表示")
    print("3. 名前で検索")
    print("4. 名前で削除")
    print("5. 名前で更新")
    print("6. 終了")
    choice = input("番号を選んでください： ")

    if choice == "1":
        name = input("名前： ")
        age = input("年齢： ")
        db.add(Person(name, age))
        print("追加しました。（自動保存済み）\n")

    elif choice == "2":
        print("\n--- 登録されている人 ---")
        for p in db.people:
            print(p.greet())
        print()

    elif choice == "3":
        name = input("検索する名前： ")
        result = db.find(name)
        if result:
            print("見つかりました：")
            print(result.greet(), "\n")
        else:
            print("見つかりませんでした。\n")

    elif choice == "4":
        name = input("削除する名前： ")
        if db.delete(name):
            print("削除しました。（自動保存済み）\n")
        else:
            print("見つかりませんでした。\n")

    elif choice == "5":
        name = input("更新する名前： ")
        new_name = input("新しい名前： ")
        new_age = input("新しい年齢： ")
        if db.update(name, new_name, new_age):
            print("更新しました。（自動保存済み）\n")
        else:
            print("見つかりませんでした。\n")

    elif choice == "6":
        print("終了します。（最終保存済み）")
        db.save()
        break

    else:
        print("無効な入力です。\n")
## 🖼 スクリーンショット


## 💬 コメント
- 追加・削除・更新のたびに自動保存されるようになった。
- 保存忘れがなくなり、実用的なデータベースの振る舞いになった。
- AIエージェントの「永続化メモリ」の基礎が完成した。
- 終了時にも最終保存されるため、データの整合性が高まった。