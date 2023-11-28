import tkinter as tk

app = tk.Tk()
# 设置标题栏
app.title("FISHC Demo")
# 显示文本
theLabel = tk.Label(app, text="我的第一个窗口程序")
# 自动调节组件尺寸和位置
theLabel.pack()
# 窗口的主事件循环,即进入消息循环
app.mainloop()
