from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)


def callback():
    var.set("吹吧你，我才不信呢")


var = StringVar()
var.set('您所下载的影片含有未成年人限制内容，\n请满十八周岁后再点击观看')
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)
photo = PhotoImage(file='R-C.gif')
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)
theButton = Button(frame2, text='我已满十八岁', command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
mainloop()
