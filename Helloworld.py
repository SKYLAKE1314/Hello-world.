import tkinter as tk

def show_hello_world():
    window = tk.Tk()
    window.title("Hello World")
    
    label = tk.Label(window, text="Hello World", font=("Arial", 24))
    label.pack(padx=20, pady=20)
    
    window.mainloop()

# 你可以根据需要更改此值以控制弹窗的数量
num_windows = 5

for _ in range(num_windows):
    show_hello_world()
