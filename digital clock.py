from cgitb import text
import tkinter as ui
import time
from unicodedata import digit
window = ui.Tk()


def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + seconds + ":" + seconds + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000 , update_clock)




digital_clock_lbl = ui.Label(window, text ="00:00:00",
                                     font="ds-digital 72 bold",
                                     background='blue' )
digital_clock_lbl.pack()

update_clock()

window.mainloop()