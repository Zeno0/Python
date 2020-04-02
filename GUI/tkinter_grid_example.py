# using tkinter module of the python to create GUI
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion) 

# tkinter._test()  comment out this line if you want to check the versions

mainWindow = tkinter.Tk()

mainWindow.title("Hello.. world..?")
mainWindow.geometry('640x480+8+200')  # here 8 means window will be 8 pixel away from left similarly, for 200 it will be from above 

lable = tkinter.Label(mainWindow,text= 'Hello.. world..?')
lable.grid(row = 0, column=0)

leftframe = tkinter.Frame(mainWindow)
leftframe.grid(row = 1, column=1)
canvas = tkinter.Canvas(leftframe, relief = 'raised', borderwidth = 1)
canvas.grid(row = 1, column=0)

rightframe = tkinter.Frame(mainWindow)
rightframe.grid(row = 1, column=2 )
button1 = tkinter.Button(rightframe, text="Button 1")
button2 = tkinter.Button(rightframe, text="Button 1")
button3 = tkinter.Button(rightframe, text="Button 1")
button1.grid(row = 0, column=0)
button2.grid(row = 1, column=0)
button3.grid(row = 2, column=0)


mainWindow.columnconfigure(0,weight = 1)
mainWindow.columnconfigure(1,weight = 1)
mainWindow.grid_columnconfigure(2,weight=1)

leftframe.config(relief = 'sunken', borderwidth = 1 )
rightframe.config(relief = 'sunken', borderwidth = 1 )
leftframe.grid(sticky = 'ns')
rightframe.grid(sticky = 'new')
rightframe.columnconfigure(0 ,weight = 1)
button2.grid(sticky = 'ew')
mainWindow.mainloop()

