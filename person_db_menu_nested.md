# Python ミニアプリ（Day37）PersonDB メニュー階層化（サブメニュー）

## 🧮 概要
PersonDB のメニューを階層化し、
「検索メニュー」「編集メニュー」を持つ本格的なアプリ構造を実現しました。
機能ごとにメニューを分離することで、操作性と拡張性が大きく向上しています。

## 🛠 使用技術
- Python
- VS Code
- クラス（Person / PersonDB）
- JSON 保存・読み込み
- 自動保存（auto-save）
- メニュー階層化（サブメニュー）
- 関数化によるコード整理

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
        self.save()

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

    def find_all(self, keyword):
        return [p for p in self.people if keyword in p.name]

    def delete(self, name):
        for p in self.people:
            if p.name == name:
                self.people.remove(p)
                self.save()
                return True
        return False

    def update(self, name, new_name, new_age):
        person = self.find(name)
        if person:
            person.name = new_name
            person.age = int(new_age)
            self.save()
            return True
        return False


# --- メニュー操作 ---
db = PersonDB()
db.load()

def search_menu():
    while True:
        print("=== 検索メニュー ===")
        print("1. 完全一致検索")
        print("2. 部分一致検索")
        print("3. 戻る")
        choice = input("番号を選んでください： ")

        if choice == "1":
            name = input("検索する名前： ")
            result = db.find(name)
            if result:
                print(result.greet(), "\n")
            else:
                print("見つかりませんでした。\n")

        elif choice == "2":
            keyword = input("検索キーワード： ")
            results = db.find_all(keyword)
            if results:
                print("\n--- 部分一致検索の結果 ---")
                for p in results:
                    print(p.greet())
                print()
            else:
                print("該当する人がいませんでした。\n")

        elif choice == "3":
            break

        else:
            print("無効な入力です。\n")


def edit_menu():
    while True:
        print("=== 編集メニュー ===")
        print("1. 名前で削除")
        print("2. 名前で更新")
        print("3. 戻る")
        choice = input("番号を選んでください： ")

        if choice == "1":
            name = input("削除する名前： ")
            if db.delete(name):
                print("削除しました。\n")
            else:
                print("見つかりませんでした。\n")

        elif choice == "2":
            name = input("更新する名前： ")
            new_name = input("新しい名前： ")
            new_age = input("新しい年齢： ")
            if db.update(name, new_name, new_age):
                print("更新しました。\n")
            else:
                print("見つかりませんでした。\n")

        elif choice == "3":
            break

        else:
            print("無効な入力です。\n")


while True:
    print("=== PersonDB メインメニュー ===")
    print("1. 人を追加")
    print("2. 全員を表示")
    print("3. 検索メニューへ")
    print("4. 編集メニューへ")
    print("5. 終了")
    choice = input("番号を選んでください： ")

    if choice == "1":
        name = input("名前： ")
        age = input("年齢： ")
        db.add(Person(name, age))
        print("追加しました。\n")

    elif choice == "2":
        print("\n--- 登録されている人 ---")
        for p in db.people:
            print(p.greet())
        print()

    elif choice == "3":
        search_menu()

    elif choice == "4":
        edit_menu()

    elif choice == "5":
        print("終了します。")
        db.save()
        break

    else:
        print("無効な入力です。\n")
## 🖼 スクリーンショット


## 💬 コメント
- メニューを階層化し、実際のアプリに近い操作体系になった。
- 検索メニューと編集メニューを分離することで、コードの見通しが大幅に改善した。
- 自動保存と組み合わせて、より実用的なデータベースアプリになった。
- AIエージェントの「機能別モジュール化」の基礎が完成した。
