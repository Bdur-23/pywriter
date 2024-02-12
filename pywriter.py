import time
import random
from pynput.keyboard import Key, Controller


keyboard = Controller()
time.sleep(3)

def deleter(n):
     for i in range(n):
          keyboard.press(Key.backspace)
          keyboard.release(Key.backspace)

def typer(text):
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

#enter your text and click anywhere in 3 seconds
typer("""enter anything""")


