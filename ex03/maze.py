import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym
def key_up(event):
    global key
    key = ""
def main_proc():
    delta = {
        ""     : [0,  0],
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    global mx, my
    global cx, cy
    if maze_lst[my+delta[key][1]][mx+delta[key][0]] == 0:
        mx, my = mx+delta[key][0], my+delta[key][1]
        cx, cy = mx*100+50, my*100+50
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)
def count_up():
    global tmr
    tmr=tmr+1
    label["text"] = tmr
    root.after(1000,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    label = tk.Label(root, font=("",80))
    label.pack()
    tmr=0
    root.after(1000, count_up)
    canv = tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv, maze_lst)
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori")
    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()

    root.mainloop()
