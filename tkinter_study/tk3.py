from tkinter import *

root = Tk()

photo = PhotoImage(file='R-C.gif')
# imgLabel = Label(root, image=photo)
# imgLabel.pack(side=RIGHT)
textLabel = Label(root, text="您所下载的影片含有未成年人限制内容，\n请满十八周岁后再点击观看", justify=LEFT, padx=10,
                  image=photo, fg='white')
textLabel.pack(side=LEFT)
mainloop()
