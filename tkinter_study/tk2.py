import tkinter as tk


class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.hi_there = tk.Button(frame, text="打招呼", bg='white', fg="blue", command=self.say_hi())
        self.hi_there.pack()

    def say_hi(self):
        print('大家晚上好啊')


# 创建窗口对象
root = tk.Tk()
app = App(root)
# 进入消息循环
root.mainloop()
