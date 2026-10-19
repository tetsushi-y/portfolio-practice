print("メモ帳ビューア（Day22）")
print("memo.txt の内容を表示します。\n")

try:
    with open("memo.txt", "r", encoding="utf-8") as f:
        content = f.read()
        if content.strip() == "":
            print("メモはまだありません。")
        else:
            print("▼ メモ内容 ▼\n")
            print(content)
except FileNotFoundError:
    print("memo.txt が見つかりません。Day21 を先に実行してください。")
