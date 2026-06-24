from tkinter import *

root = Tk()
root.title("Premium Calculator")
root.geometry("350x500")
root.config(bg="#1e1e2f")
root.resizable(False, False)

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

entry = Entry(root,
              textvariable=equation,
              font=("Arial", 24),
              bd=10,
              relief=FLAT,
              justify="right",
              bg="#2d2d44",
              fg="white")
entry.pack(fill="both", padx=10, pady=20, ipady=15)

frame = Frame(root, bg="#1e1e2f")
frame.pack()

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+', '%']
]

for row in buttons:
    row_frame = Frame(frame, bg="#1e1e2f")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        Button(
            row_frame,
            text=btn,
            font=("Arial",18,"bold"),
            bg="#3b3b5c",
            fg="white",
            bd=0,
            padx=20,
            pady=20,
            command=lambda b=btn:
                clear() if b=="C"
                else equal() if b=="="
                else press(b)
        ).pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()