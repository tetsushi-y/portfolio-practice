import time

print("ストップウォッチを開始します。Enterキーでスタートします。")
input()

start = time.time()
print("計測中... Enterキーでストップします。")

input()
end = time.time()

elapsed = end - start

print(f"経過時間: {elapsed:.2f} 秒")
