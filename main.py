from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
 
root.title('Calculator')

 
num1 = StringVar()

"""Top row of buttons""" 
topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay = Entry(frame, textvariable = num1, bd = 20, insertwidth = 1, font = 1)
txtDisplay.pack(side = TOP)

button1 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "1", fg = "black")
button1.pack(side = LEFT)
button2 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "2", fg = "black")
button2.pack(side = LEFT)
button3 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "3", fg = "black")
button3.pack(side = LEFT)
button4 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "C", fg = "black")
button4.pack(side = LEFT)

"""Second row of buttons"""
frame2 = Frame(root)
frame2.pack(side = TOP)

button1 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "4", fg = "black")
button1.pack(side = LEFT)
button2 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "5", fg = "black")
button2.pack(side = LEFT)
button3 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "6", fg = "black")
button3.pack(side = LEFT)
button4 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "*", fg = "black")
button4.pack(side = LEFT)

"""Third row of buttons"""
frame3 = Frame(root)
frame3.pack(side = TOP)

button1 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "7", fg = "black")
button1.pack(side = LEFT)
button2 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "8", fg = "black")
button2.pack(side = LEFT)
button3 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "9", fg = "black")
button3.pack(side = LEFT)
button4 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "/", fg = "black")
button4.pack(side = LEFT)

"""Fourth row of buttons"""
frame4 = Frame(root)
frame4.pack(side = TOP)

button1 = Button(frame4, padx = 16, pady = 16, bd = 8, text = "+", fg = "black")
button1.pack(side = LEFT)
button2 = Button(frame4, padx = 16, pady = 16, bd = 8, text = "0", fg = "black")
button2.pack(side = LEFT)
button3 = Button(frame4, padx = 16, pady = 16, bd = 8, text = "-", fg = "black")
button3.pack(side = LEFT)
button4 = Button(frame4, padx = 16, pady = 16, bd = 8, text = "=", fg = "black")
button4.pack(side = LEFT)

root.mainloop()

