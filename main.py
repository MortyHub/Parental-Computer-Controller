import time
import os
from tkinter import *

window = Tk()

def Start():
    try:
        timer = int(textField.get("1.0", "end-1c"))
        success = Label(window, text="Starting...", fg='Green', font=("Helvetica", 16))
        success.place(x=200,y=200)
        time.sleep(5)
        window.destroy()
        time.sleep(timer)
        os.system("shutdown /s /t 1")
    except:
        error = Label(window, text='This is not a number', fg='Red', font=('Helvetica', 10))
        error.place(x=200,y=200)
        


# Button
enter = Button(window, text='Press this to start', command=Start)
enter.place(x=200,y=150)

# Label Uptop
lbl=Label(window, text="Insert Time In Seconds", fg="Blue", font=("Helvetica", 16))
lbl.place(x=150, y=50)

# Text Entry
textField = Text(window, height=1, width=25)
textField.place(x=180, y=100)



# Main Attributes
window.title("Computer Timer")
window.geometry("200x150")
window.mainloop()

