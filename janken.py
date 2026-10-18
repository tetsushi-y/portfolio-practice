import random

hands = ["グー", "チョキ", "パー"]

print("じゃんけんゲーム")
print("0: グー, 1: チョキ, 2: パー")

player = int(input("あなたの手を選んでください（0〜2）: "))
computer = random.randint(0, 2)

print("あなた:", hands[player])
print("コンピュータ:", hands[computer])

# 勝敗判定
if player == computer:
    print("結果: あいこ")
elif (player == 0 and computer == 1) or \
     (player == 1 and computer == 2) or \
     (player == 2 and computer == 0):
    print("結果: あなたの勝ち！")
else:
    print("結果: コンピュータの勝ち")
