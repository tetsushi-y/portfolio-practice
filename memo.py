print("メモ帳アプリ（Day21）")
print("書きたい内容を入力してください。")
print("終了したい場合は空のまま Enter を押してください。\n")

with open("memo.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("> ")
        if text == "":
            print("メモを保存して終了します。")
            break
        f.write(text + "\n")
        print("保存しました。")
