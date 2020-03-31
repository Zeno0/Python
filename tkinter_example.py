# using tkinter module of the python to create GUI
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()  comment out this line if you want to check the versions

mainWindow = tkinter.Tk()

mainWindow.title("Hello.. world..?")
mainWindow.geometry('640x480+8+200')  # here 8 means window will be 8 pixel away from left similarly, for 200 it will be from above 

lable = tkinter.Label(mainWindow,text= 'Hello.. world..?')
lable.pack(side="top")

# Two ways to create GUI is there, BELOW one is where frame is not used
# comment line 35 to 47 and uncomment the line 21 to 31 
# to check below method

#canvas = tkinter.Canvas(mainWindow, relief = 'raised', borderwidth = 1)
#canvas.pack(side="left",fill = tkinter.Y)                 #  differnet types of arguments for pack method
#canvas.pack(side="left",fill = tkinter.X,expand = True)
#canvas.pack(side="left")

#button1 = tkinter.Button(mainWindow, text="Button 1") 
#button2 = tkinter.Button(mainWindow, text="Button 1")
#button3 = tkinter.Button(mainWindow, text="Button 1")
#button1.pack(side="left", anchor='n')
#button2.pack(side="left", anchor='s')
#button3.pack(side="left", anchor='e')

# In this frame is used 

leftframe = tkinter.Frame(mainWindow)
leftframe.pack(side= "left", anchor="n", fill= tkinter.Y, expand= False)
canvas = tkinter.Canvas(leftframe, relief = 'raised', borderwidth = 1)
canvas.pack(side="left",anchor= "n")

rightframe = tkinter.Frame(mainWindow)
rightframe.pack(side= "right", anchor="n", expand= True)
button1 = tkinter.Button(rightframe, text="Button 1")
button2 = tkinter.Button(rightframe, text="Button 1")
button3 = tkinter.Button(rightframe, text="Button 1")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")


mainWindow.mainloop()

