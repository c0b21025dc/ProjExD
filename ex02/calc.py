import tkinter as tk
import tkinter.messagebox as tkm
def click_number(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END,num)
def click_equal(event):
    eqn =entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END,res)
def click_clear(event):
    entry.delete(0,tk.END)
def click_backspace(event):
    end = len(entry.get())-1
    entry.delete(end,tk.END)
root = tk.Tk()
root.geometry("400x800")
r ,c= 1,0
entry = tk.Entry(root,width=10,font=("", 40),justify="right")
entry.grid(row=0,column=0,columnspan=3)
numbers = list(range(9, -1, -1))
operators = [".","","+","-","*"]
for i, num in enumerate(numbers+operators,1):
    btn = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    btn.bind("<1>",click_number)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 ==0:
        r += 1
        c = 0
btn = tk.Button(root,text=f"=",font=("",30),width=4,height=2)
btn.bind("<1>",click_equal)
btn.grid(row=r-5,column=c+3)
#clear機能
btn = tk.Button(root,text=f"c",font=("",30),width=4,height=2)
btn.bind("<1>",click_clear)
btn.grid(row=r-2,column=c+3)
#backspace機能
btn = tk.Button(root,text=f"BS",font=("",30),width=4,height=2)
btn.bind("<1>",click_backspace)
btn.grid(row=r-2,column=c+2)
#割り算機能
btn = tk.Button(root,text=f"/",font=("",30),width=4,height=2)
btn.bind("<1>",click_number)
btn.grid(row=r-1,column=c+3)

root.mainloop()