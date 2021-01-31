import tkinter 

def handle_click(event):
    global user
    user={'name':name_entry.get(),'password': password_entry.get()}
def create():
    root = tkinter.Toplevel()
    e1 = tkinter.Label(root,text = '已记录').pack()
    button2 = tkinter.Button(root,text = '关闭',command = top.destroy).pack()
top = tkinter.Tk()
top.title('简简单单打个卡')
name_label = tkinter.Label(text = 'Name')
name_entry = tkinter.Entry()
password_label = tkinter.Label(text = 'password')
password_entry = tkinter.Entry()
button = tkinter.Button(text = '打卡',command = create)
button.bind("<Button-1>",handle_click)
name_label.pack()
name_entry.pack()
password_label.pack()
password_entry.pack()
button.pack()
user = {}


