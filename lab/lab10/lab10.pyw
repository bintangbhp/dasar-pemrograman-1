"""
Lab 10 DDP1/FPROG1 2020
- draw elastic (rubber) shapes on a canvas by
 a left mouse-click and dragging,
- move the last drawn shape by a right mouse-click
"""

from tkinter import *
from tkinter.colorchooser import askcolor
class DrawRubberShapes(object):
    
    # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 10: Drawing Rubber Shapes") # Set a title
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
        # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('red')
    
        def colorCommand():
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color
        
        colorButton = Button(frame1, text = "Color",
            command=colorCommand, bg = self.fillColor.get(), font = 'CourierNew 15 bold',
            fg = 'white')
        colorButton.grid(row=1,column=1,columnspan=2)
        
        # Create radio buttons for geometrical shapes
        # Rectangle button
        self.v1 = StringVar(frame1, 'L')
        rbRectangle = Radiobutton(frame1, text = "Rectangle",
            variable = self.v1, value = 'R',
            command = self.processRadiobutton)
        rbRectangle.grid(row = 1, column = 5)

        # Oval button
        rbOval = Radiobutton(frame1, text = "Oval",
            variable = self.v1, value = 'O',
            command = self.processRadiobutton)
        rbOval.grid(row = 1, column = 4)

        # Line button
        rbLine = Radiobutton(frame1, text = "Line",
            variable = self.v1, value = 'L',
            command = self.processRadiobutton)
        rbLine.grid(row = 1, column = 3)

        # Membuat clear button untuk menghapus gambar
        clearButton = Button(frame1, text = "Clear",
            command= self.delete, bg = 'blue', font = 'CourierNew 15 bold',
            fg = 'white')
        clearButton.grid(row=1,column=6,columnspan=2) 

        # Create a canvas, bound to mouse events
        canvas = Canvas(window, width=400, height=300)
        self.canvas = canvas
        self.canvas.pack()
        self.canvas.bind('<ButtonPress-1>', self.onStart) # left click
        self.canvas.bind('<B1-Motion>', self.onGrow) # Drag
        self.canvas.bind('<ButtonPress-3>', self.onMove) # Right click
        
        # For remembering the last drawing
        self.drawn = None   
        
        self.shape = self.canvas.create_line
        
        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == 'R': 
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'O':
            self.shape = self.canvas.create_oval
        else:
            self.shape = self.canvas.create_line
            
    def delete(self):
        self.canvas.delete('all')
    
    def onStart(self, event):
        self.start = event
        self.drawn = None

    # Elastic drawing: delete and redraw, repeatedly
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        
        self.x = self.start.x + abs(self.start.x - event.x)/2
        self.y = self.start.y + abs(self.start.y - event.y)/2

        # Memberi warna outline yang sama
        if self.v1.get() == 'L':
            objectId = self.shape(self.start.x, self.start.y, event.x,
                event.y, fill=self.fillColor.get())
        else:
            objectId = self.shape(self.start.x, self.start.y, event.x,
                event.y, fill=self.fillColor.get(), outline = '')
        self.drawn = objectId
    
    # Move the shape to the click spot
    def onMove(self, event):
        if self.drawn:
            canvas = event.widget
            diffX, diffY = (event.x-self.x), (event.y-self.y)
            canvas.move(self.drawn, diffX, diffY)

            self.start = event

            self.x , self.y = self.start.x , self.start.y


if __name__ == '__main__':
    DrawRubberShapes()  