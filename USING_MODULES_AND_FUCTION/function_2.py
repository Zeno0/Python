import tkinter
# function parabola
def parabola(x):
    y=x*x/50 # dividing by 50 to make graph visible in the window
    return y

# function draw_axes
def draw_axes(canvas):
    canvas.update()
    x = canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x,-y,x,y))
    canvas.create_line(-x,0,x,0,fill="black")
    canvas.create_line(0,y,0,-y,fill="black")
    print(locals())
# function plot
def plot(canvas,x,y):
    canvas.create_line(x,y,x+1,y+1,fill="red")


# GUI
mainWindow = tkinter.Tk()
mainWindow.title("parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas) # function call

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480)
canvas2.grid(row=0, column=1)
draw_axes(canvas2)
print(repr(canvas),repr(canvas2))
for i in range(-100,100):
    y = parabola(i)  # function call
    plot(canvas,i,-y)
    plot(canvas2,i,y)

mainWindow.mainloop()