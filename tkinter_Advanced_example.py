import tkinter
import os
# basic of creating a window
mainWindow = tkinter.Tk()
mainWindow.title("Example")
mainWindow.geometry("640x480+10+100")
mainWindow['padx'] = 8

# creating a label
lable = tkinter.Label(mainWindow, text='tkinter Grid Example')
lable.grid(row = 0, column= 1, columnspan=3)

# configuring mainWindow to grid
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=10)
mainWindow.rowconfigure(2,weight=1)
mainWindow.rowconfigure(3,weight=3)
mainWindow.rowconfigure(4,weight=3)

# creating filelist
filelist = tkinter.Listbox(mainWindow)
filelist.grid(row=1, column=0, sticky='nsew', rowspan=2)
filelist.config(border=2, relief='sunken')
for i in os.listdir("C:\Windows\System32"):
    filelist.insert(tkinter.END,i)

# creating listscroll
listscroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=filelist.yview)
listscroll.grid(row=1, column=1, sticky='nsew', rowspan=2)
filelist['yscrollcommand'] = listscroll.set

# creating radio buttons
opframe = tkinter.LabelFrame(mainWindow, text="File Details")
opframe.grid(row=1, column=2, sticky='ne')
rbval = tkinter.IntVar()
rbval.set(3)
radio1 = tkinter.Radiobutton(opframe, text='Filename', value=1, variable=rbval)
radio2 = tkinter.Radiobutton(opframe, text='path', value=2, variable=rbval)
radio3 = tkinter.Radiobutton(opframe, text='timestamp', value=3, variable=rbval)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# creating resukt label
res_label = tkinter.Label(mainWindow, text="Result")
res_label.grid(row=2, column=2, sticky='nw')
result= tkinter.Entry(mainWindow)
result.grid(row=2, column= 2, sticky= 'sw')

# creating time scroller 
timeframe = tkinter.LabelFrame(mainWindow, text = "Time")
timeframe.grid(row=3, column=0, sticky= "new")
hour = tkinter.Spinbox(timeframe, width=2, values=tuple(range(0,24)))
minute = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
second = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
hour.grid(row= 0, column=0)
tkinter.Label(timeframe, text=':').grid(row=0, column=1)
minute.grid(row=0, column=2)
tkinter.Label(timeframe, text=':').grid(row=0, column=3)
second.grid(row=0, column=4)
timeframe["padx"] = 36

# creating date scroller 
dateframe = tkinter.Frame(mainWindow)
dateframe.grid(row=4, column=0, sticky='new')
day = tkinter.Label(dateframe, text="day").grid(row=0, column=0, sticky='w')
month = tkinter.Label(dateframe, text="month").grid(row=0, column=1, sticky='w')
year = tkinter.Label(dateframe, text="year").grid(row=0, column=2, sticky="w")
dayspin = tkinter.Spinbox(dateframe, width=5, from_=1, to=31).grid(row=1, column=0)
monthpin = tkinter.Spinbox(dateframe, width=5, values=("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec" )).grid(row=1, column=1)
yearpin = tkinter.Spinbox(dateframe, width=5, from_=2000, to=2099).grid(row=1, column=2)
dateframe["padx"] = 36 

# creating ok and cancel button
okbut = tkinter.Button(mainWindow, text='OK').grid(row=4, column=3, sticky='e')
cancelbut = tkinter.Button(mainWindow, text="cancel", command=mainWindow.destroy).grid(row=4, column=4, sticky='w')


mainWindow.mainloop()