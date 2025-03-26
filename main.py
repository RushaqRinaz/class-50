# 3. add widgets

from tkinter import *

window=Tk()
window.title('Tkinter sample window')
window.geometry('300x300')

# Label
greeting=Label(text="Hello user", fg='black', bg='white')
# Button
button=Button(text="Click me", bg="black", fg='white')
# Entry
entry=Entry(fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label=Label(master=frame, text='sample Frame')
label.pack()

textbox=Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()