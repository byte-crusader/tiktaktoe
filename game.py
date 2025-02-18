from tkinter import *

root = Tk()
root.configure(bg="#FFC0CB")
root.title("TikTakToe")

e = Label(root, text="game display")
e.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

def add_char(num1, num2):
    print(li[num1][num2])
    # li[int(num1)][].configure(text="♥")
    print("oh yes", num1, num2)
    return

li = []
num = 1
active_symbol = ""
x = "♥"
o = "★"


for i in range(3):
    for j in range(3):
        button_1 = Button(root, text=active_symbol, padx=40, pady=20, command= lambda btn1 = i, btn2 = j :  add_char(btn1, btn2))
        button_1.grid(row=i, column=j)
        li.append(button_1)

for x in range(len(li)):
    # li[x].configure(text="♥")
    li[x].configure(bg="#FFC0CB")
print(f"\033[95m{li[0]}!\033[0m")


root.mainloop()
