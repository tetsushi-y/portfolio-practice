import time

print("タイマーを設定します。何秒にしますか？")
seconds = int(input("秒数を入力してください: "))

while seconds > 0:
    print(f"残り {seconds} 秒")
    time.sleep(1)
    seconds -= 1

print("時間になりました！")
