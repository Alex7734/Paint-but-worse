import tkinter as tk
from tkinter import ttk, colorchooser

# THIS IS SO FUCKING JS LIKE xD
class main:
    # setting up the program
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint) #drwaing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)

    # window
    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=tk.ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y
    
    # reseting or cleaning the canvas 
    def reset(self,e):  
        self.old_x = None
        self.old_y = None      

    # change Width of pen through slider
    def changeW(self,e):
        self.penwidth = e
           

    def clear(self):
        self.c.delete(tk.ALL)

    # changing the pen color
    def change_fg(self):  
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    # changing the background color canvas
    def change_bg(self): 
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    # painting
    def drawWidgets(self):
        self.controls = tk.Frame(self.master,padx = 5,pady = 5)
        tk.Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=tk.VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack(side=tk.LEFT)
        
        self.c = tk.Canvas(self.master,width=1024,height=600,bg=self.color_bg,)
        self.c.pack(fill=tk.BOTH,expand=True)

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        colormenu = tk.Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)
        optionmenu = tk.Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 
        

if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.title('Application')
    root.mainloop()

    