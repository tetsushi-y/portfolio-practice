import csv

print("CSV 書き込みツール（Day23）")
print("名前と年齢を入力すると data.csv に追記します。")
print("終了したい場合は空のまま Enter を押してください。\n")

with open("data.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    while True:
        name = input("名前: ")
        if name == "":
            print("終了します。")
            break

        age = input("年齢: ")
        if age == "":
            print("終了します。")
            break

        writer.writerow([name, age])
        print("保存しました。\n")
