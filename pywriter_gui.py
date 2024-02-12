import time
import random
from pynput.keyboard import Key, Controller
import tkinter as tk

window = tk.Tk()
window.title("Typer")
window.attributes('-fullscreen',True)

keyboard = Controller()


def deleter(n):
     for i in range(n):
          keyboard.press(Key.backspace)
          keyboard.release(Key.backspace)

#types while making and fixing mistakes
def typer_a(text):
     for char in text:
          
          if random.randint(1,20) == 14:
               
               ind = text.index(char)
               tlist = [text[i] for i in [ind-1,ind-2,ind+1,ind+2,ind+3]]
               rans = "".join(tlist[i] for i in range(random.randrange(2,6)))
               
               keyboard.type(rans)
               time.sleep(1)
               deleter(len(rans))
               time.sleep(1)
          
          keyboard.type(char) 
          time.sleep(0.1)

#types without mistakes
def typer_b(text):
     for char in text:          
          keyboard.type(char) 
          time.sleep(0.1)


def submit():
     time.sleep(3)
     s1 = message.get()
     if var1.get() == 0:
          typer_b(s1)
     else:
          typer_a(s1)


info = tk.Label(window, text="It starts writing 3 seconds after clicking submit").place(x=90,y=80)
message = tk.StringVar()
ai_text = tk.Entry(window, bd=1, textvariable=message)
ai_text.place(x=100,y=100)

submit_button = tk.Button(window, text="Submit", command=submit).place(x=230,y=100)

output = tk.Label(window, textvariable=message).place(x=90,y=140)

var1 = tk.IntVar()
mistake_btn = tk.Checkbutton(window, text='type by making and fixing mistakes',variable=var1, onvalue=1, offvalue=0)
mistake_btn.place(x=300,y=100)


exit_btn = tk.Button(window, bg="red", fg="white", text="X", height=1, width=5, command=lambda: window.destroy()).place(x=1322,y=0)
window.mainloop()

