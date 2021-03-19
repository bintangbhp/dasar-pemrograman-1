from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename

class Scribble(object):
    '''a simple pen drawing application'''
    def __init__(self):
        master = Tk()
        master.title("Simple Pen (Finger) Scribble")
        
        # mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0, 0
        self.color = '#8000FF' # Warna awal
        
        # create canvas 400X250 and bind mouse events to handlers
        self.canvas = Canvas(master, width = 400, height = 250)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)    
        self.canvas.pack(expand=True, fill=BOTH)
        
        # create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)
        
        # Membuat button clear
        self.bt_clear = Button(master=frame1, text= 'Clear', bg= 'Orange', fg= 'White', font='CourierNew 15 bold', command = self.delete)
        self.bt_clear.pack(side=LEFT, padx=5) # Menaruh button dan memberi jarak
        
        # Membuat button color
        self.bt_color = Button(master=frame1, text= 'Color', bg= self.color, fg = 'White', font='CourierNew 15 bold', command = self.change_color)
        self.bt_color.pack(side=LEFT, padx=5)
        
        # Membuat button save
        self.bt_save = Button(master=frame1, text= 'Save', bg= 'Blue', fg = 'White', font='CourierNew 15 bold', command = self.saveToPS)
        self.bt_save.pack(side=LEFT, padx=5)

        self.message = Label(master, text = 'Press and drag the left mouse-button to draw', fg='Blue')
        self.message.pack(side = BOTTOM)
        
        # start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position
        as the start of the curve'''
        self.oldx , self.oldy = event.x, event.y # Menyimpan posisi mouse ketika di click

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
        connecting the previous mouse position to the new one'''
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill= self.color) # Membuat garis
        self.oldx, self.oldy = event.x, event.y # Menyimpan mouse yang baru

    def delete(self):
        '''clear the canvas'''
        self.canvas.delete('all') # Menghapus gambar   
    
    def change_color(self):
        '''change the drawing color using the color chooser,
        also change the background color of the color button'''
        self.color = askcolor()[-1] #get the hex value from the color chooser
        self.bt_color['bg'] = self.color # Mengganti warna
    
    def saveToPS(self):
        fileName = asksaveasfilename()
        self.canvas.update()
        self.canvas.postscript(file = fileName)

if __name__ == "__main__":
    Scribble()