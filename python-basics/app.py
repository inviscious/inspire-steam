from tkinter import *

def hello():
    print("Hello from Jamey")

root = Tk()
root.geometry("600x600")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text="Say Hello",command="Hello")
button_one.pack()

root.mainloop()