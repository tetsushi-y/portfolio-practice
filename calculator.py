import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"結果: {result}")
    except Exception:
        label_result.config(text="エラー: 計算できません")

root = tk.Tk()
root.title("ミニ電卓")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.pack(pady=10)

button = tk.Button(root, text="計算する", command=calculate, font=("Arial", 14))
button.pack(pady=5)

label_result = tk.Label(root, text="結果: ", font=("Arial", 16))
label_result.pack(pady=10)

root.mainloop()
