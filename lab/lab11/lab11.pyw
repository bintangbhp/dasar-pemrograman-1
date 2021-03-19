from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import *
import time
from tkinter.filedialog import asksaveasfilename

class DrawRubberShapes(object):
    
    # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 11: Select, Move, and Animate") # Set a title
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
        # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('green')
    
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

        # Membuat clear all button untuk menghapus seluruh gambar
        clearButton = Button(frame1, text = "Clear All",
            command= self.deleteAll, bg = 'maroon', font = 'CourierNew 15 bold',
            fg = 'white')
        clearButton.grid(row=1,column=6,columnspan=2) 

        # Create a canvas
        canvas = Canvas(window, width=400, height=300, relief= RIDGE, bd = 3)
        self.canvas = canvas
        self.canvas.pack()
        
        # Bound to mouse event
        self.canvas.bind('<ButtonPress-1>', self.onStart) # left click
        self.canvas.bind('<B1-Motion>', self.onGrow) # Drag
        self.canvas.bind('<ButtonPress-3>', self.selectClosest) # Right click
        self.canvas.bind('<B3-Motion>', self.moveShape)
        self.canvas.bind('<ButtonPress-2>', self.animate)

        # Bound to key event
        window.bind('<KeyPress-h>', self.popUpWindow)
        window.bind('<KeyPress-d>', self.delete)
        window.bind('<KeyPress-s>', self.saveToPS)

        self.text = self.canvas.create_text(60,12,text= 'Press h for help', tags = 'string', font= 'CourierNew 12')
        
        # For remembering the last drawing
        self.drawn = None
        self.waktu = time
        self.shape = self.canvas.create_line
        
        window.mainloop()

    # Memunculkan pop up window
    def popUpWindow(self,event):
        showinfo("Select, Move, and Animate", "Mouse commands:\n  Left+Drag = Draw new rubber\n  Right = Select shape\n  Right+Drag = Drag the selected shape\n  Midle = Move the selected shape with animation\n\nKeyboard commands:\n  d = Delete the selected shape\n  h = Help\n  s = Save as a PostScript file")

    def processRadiobutton(self):
        if self.v1.get() == 'R': 
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'O':
            self.shape = self.canvas.create_oval
        elif self.v1.get() == 'L':
            self.shape = self.canvas.create_line
    
    # Menghapus seluruh gambar di canvas
    def deleteAll(self):
        self.canvas.delete('shape')
    
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
                event.y, fill=self.fillColor.get(), tags = 'shape')
        else:
            objectId = self.shape(self.start.x, self.start.y, event.x,
                event.y, fill=self.fillColor.get(), outline = '', tags = 'shape')
        self.drawn = objectId
    
    # Find the closest shape
    def selectClosest(self, event):
        canvas = event.widget
        self.drawn = self.canvas.find_closest(event.x,event.y)
        if self.canvas.gettags(self.drawn)[0] == 'string':
            self.drawn = None
        self.x , self.y = event.x , event.y
        self.start = event

    # Menghapus gambar yang dipilih
    def delete(self, event):
        self.canvas.delete(self.drawn)
        self.drawn = None

    # Memindahkan gambar yang telah dipilih
    def moveShape(self, event):
        canvas = event.widget
        self.canvas.move(self.drawn, event.x-self.x, event.y-self.y)
        self.x , self.y = event.x, event.y
        self.start = event

    # Menyimpan gambar
    def saveToPS(self,event):
        fileName = asksaveasfilename()
        self.canvas.update()
        self.canvas.postscript(file = fileName)

    def animate(self, event):
        diffX, diffY = (event.x-self.x),(event.y-self.y)

        for i in range(0,10):
            self.waktu.sleep(0.04)
            self.canvas.move(self.drawn, diffX/10, 0)
            self.canvas.update()
        for i in range(0,10):
            self.waktu.sleep(0.04)
            self.canvas.move(self.drawn, 0, diffY/10)
            self.canvas.update() 

        self.x = event.x
        self.y = event.y
    
if __name__ == '__main__':
    DrawRubberShapes()