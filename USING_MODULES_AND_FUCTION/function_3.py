import tkinter
import math
# function parabola
def parabola(page,size):
    for i in range(-size*50,size*50):
        i/=50
        y=i*i/(size-50) # dividing by 50 to make graph visible in the window
        plot(page,i,y)

# function  circle
def circle(page,r,g,h,colour="red"):
    # for x in range(g*100,(g+r)*100):
    #     x/=100
    #     y = h + (math.sqrt(r ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2*h-y)
    #     plot(page, 2*g-x, y)
    #     plot(page, 2*g-x, 2*h-y)
    # ANother easy way to create circle is:
    page.create_oval(g+r,h+r,g-r,h-r,outline=colour,width=2)
    

# function draw_axes
def draw_axes(page):
    page.update()
    x = page.winfo_width() / 2
    y = page.winfo_height() / 2
    page.configure(scrollregion=(-x,-y,x,y))
    page.create_line(-x,0,x,0,fill="black")
    page.create_line(0,y,0,-y,fill="black")

# function plot
def plot(page,x,y):
    page.create_line(x,-y,x+1,-y+1,fill="red")


# GUI
mainWindow = tkinter.Tk()
mainWindow.title("parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas) # function call
parabola(canvas,100)
parabola(canvas,200)
parabola(canvas,300)
parabola(canvas,400)
parabola(canvas,500)
parabola(canvas,600)
parabola(canvas,700)
parabola(canvas,800)
circle(canvas, 100,100,100,"green")
circle(canvas, 100,-100,-100,"yellow")
circle(canvas, 10,-30,30,"blue")
circle(canvas, 30,0,0)

mainWindow.mainloop()