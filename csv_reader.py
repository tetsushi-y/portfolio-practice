import csv

print("CSV 読み込みツール（Day24）")
print("data.csv の内容を表示します。\n")

try:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) == 0:
            print("CSV はまだ空です。")
        else:
            print("▼ CSV 内容 ▼\n")
            for row in rows:
                print(f"名前: {row[0]}, 年齢: {row[1]}")
except FileNotFoundError:
    print("data.csv が見つかりません。Day23 を先に実行してください。")
