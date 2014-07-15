#word_clock
#created december 16, 2013
from datetime import datetime
from tkinter import *

s1 = 'IT IS HALFTEN'
s2 = 'QUARTERTWENTY'
s3 = 'FIVE  MINUTES'
s4 = 'PAST     TO  '
s5 = 'ONE TWO THREE'
s6 = 'FOURFIVESEVEN'
s7 = 'SIXEIGHT NINE'
s8 = 'TENELEVENAMPM'
s9 = 'TWELVE OCLOCK'

words = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
# print (str(hour) + ':' + str(minute))

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        #self.timer()
        #self.root.mainloop()

    def initUI(self):

        self.parent.title("Word Clock")
        self.pack(fill=BOTH, expand=1)

        defualt_fill='#393939'
        defualt_font='Courier 70 bold'
        height=75
        width=47

        #height = 100
        #width = (height*47)/75
        
        self.canvas = Canvas(self, cursor='', bg='#292929')
        #first row
        self.itis = self.canvas.create_text(width, height, anchor=W, font=defualt_font,
                           text=words[0][:5], fill=defualt_fill)
        self.half = self.canvas.create_text(width*7, height, anchor=W, font=defualt_font,
                           text=words[0][5:10], fill=defualt_fill)
        self.ten1 = self.canvas.create_text(width*13, height, anchor=W, font=defualt_font,
                           text=words[0][10:], fill=defualt_fill)
        #second row
        self.quarter = self.canvas.create_text(width, height*2, anchor=W, font=defualt_font,
                           text=words[1][:7], fill=defualt_fill)
        self.twenty = self.canvas.create_text(width*9.4, height*2, anchor=W, font=defualt_font,
                           text=words[1][7:], fill=defualt_fill)
        #third row
        self.five1 = self.canvas.create_text(width, height*3, anchor=W, font=defualt_font,
                           text=words[2][:4], fill=defualt_fill)
        self.minutes = self.canvas.create_text(width*8.2, height*3, anchor=W, font=defualt_font,
                           text=words[2][6:], fill=defualt_fill)
        #fourth row
        self.past = self.canvas.create_text(width, height*4, anchor=W, font=defualt_font,
                           text=words[3][:4], fill=defualt_fill)
        self.to = self.canvas.create_text(width*11.75, height*4, anchor=W, font=defualt_font,
                           text=words[3][9:], fill=defualt_fill)
        #fifth row
        self.one = self.canvas.create_text(width, height*5, anchor=W, font=defualt_font,
                           text=words[4][:3], fill=defualt_fill)
        self.two = self.canvas.create_text(width*5.8, height*5, anchor=W, font=defualt_font,
                           text=words[4][4:7], fill=defualt_fill)
        self.three = self.canvas.create_text(width*10.6, height*5, anchor=W, font=defualt_font,
                           text=words[4][8:], fill=defualt_fill)
        #sixth row
        self.four = self.canvas.create_text(width, height*6, anchor=W, font=defualt_font,
                           text=words[5][:4], fill=defualt_fill)
        self.five2 = self.canvas.create_text(width*5.8, height*6, anchor=W, font=defualt_font,
                           text=words[5][4:8], fill=defualt_fill)
        self.seven = self.canvas.create_text(width*10.6, height*6, anchor=W, font=defualt_font,
                           text=words[5][8:], fill=defualt_fill)
        #seventh row
        self.six = self.canvas.create_text(width, height*7, anchor=W, font=defualt_font,
                           text=words[6][:3], fill=defualt_fill)
        self.eight = self.canvas.create_text(width*4.6, height*7, anchor=W, font=defualt_font,
                           text=words[6][3:9], fill=defualt_fill)
        self.nine = self.canvas.create_text(width*11.8, height*7, anchor=W, font=defualt_font,
                           text=words[6][9:], fill=defualt_fill)
        #eigth row
        self.ten2 = self.canvas.create_text(width, height*8, anchor=W, font=defualt_font,
                           text=words[7][:3], fill=defualt_fill)
        self.eleven = self.canvas.create_text(width*4.6, height*8, anchor=W, font=defualt_font,
                           text=words[7][3:9], fill=defualt_fill)
        self.am = self.canvas.create_text(width*11.8, height*8, anchor=W, font=defualt_font,
                           text=words[7][9:11], fill=defualt_fill)
        self.pm = self.canvas.create_text(width*14.1, height*8, anchor=W, font=defualt_font,
                           text=words[7][11:], fill=defualt_fill)
        #ninth row
        self.twelve = self.canvas.create_text(width, height*9, anchor=W, font=defualt_font,
                           text=words[8][:6], fill=defualt_fill)
        self.oclock = self.canvas.create_text(width*9.4, height*9, anchor=W, font=defualt_font,
                           text=words[8][7:], fill=defualt_fill)

        #extra letters
        self.canvas.create_text(width*3.45, height, anchor=W, font=defualt_font,
                           text='V  T', fill=defualt_fill)
        self.canvas.create_text(width*5.75, height*3, anchor=W, font=defualt_font,
                           text='GO', fill=defualt_fill, activefill='#EAEAEA')
        self.canvas.create_text(width*5.79, height*4, anchor=W, font=defualt_font,
                           text='NOLES  MO', fill=defualt_fill, activefill='#EAEAEA')
        self.canvas.create_text(width*4.58, height*5, anchor=W, font=defualt_font,
                           text='S   C', fill=defualt_fill)
        self.canvas.create_text(width*10.5, height*7, anchor=W, font=defualt_font,
                           text='Z', fill=defualt_fill)
        self.canvas.create_text(width*8.15, height*9, anchor=W, font=defualt_font,
                           text='P', fill=defualt_fill)
        
        
        self.canvas.pack(fill=BOTH, expand=1)
        

def timer(ex):
    clear_all(ex)
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    default_fill='#EAEAEA'
    ex.canvas.itemconfigure(ex.itis, fill=default_fill)
    

    #minutes
    if minute >= 55:
        changeColor(ex, ex.five1)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.to)
        hour += 1
    elif minute >= 50:
        changeColor(ex, ex.ten1)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.to)
        hour += 1
    elif minute >= 45:
        changeColor(ex, ex.quarter)
        changeColor(ex, ex.to)
        hour += 1
    elif minute >= 40:
        changeColor(ex, ex.twenty)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.to)
        hour += 1
    elif minute >= 30:
        changeColor(ex, ex.half)
        changeColor(ex, ex.past)
    elif minute >= 25:
        changeColor(ex, ex.twenty)
        changeColor(ex, ex.five1)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.past)
    elif minute >= 20:
        changeColor(ex, ex.twenty)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.past)
    elif minute >= 15:
        changeColor(ex, ex.quarter)
        changeColor(ex, ex.past)
    elif minute >= 10:
        changeColor(ex, ex.ten1)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.past)
    elif minute >= 5:
        changeColor(ex, ex.five1)
        changeColor(ex, ex.minutes)
        changeColor(ex, ex.past)
    elif minute >= 0:
        changeColor(ex, ex.oclock)

    
    #hours
    if hour == 1 or hour == 13:
        ex.canvas.itemconfigure(ex.one, fill=default_fill)
    elif hour == 2 or hour == 14:
        ex.canvas.itemconfigure(ex.two, fill=default_fill)
    elif hour == 3 or hour == 15:
        ex.canvas.itemconfigure(ex.three, fill=default_fill)
    elif hour == 4 or hour == 16:
        ex.canvas.itemconfigure(ex.four, fill=default_fill)
    elif hour == 5 or hour == 17:
        ex.canvas.itemconfigure(ex.five2, fill=default_fill)
    elif hour == 6 or hour == 18:
        ex.canvas.itemconfigure(ex.six, fill=default_fill)
    elif hour == 7 or hour == 19:
        ex.canvas.itemconfigure(ex.seven, fill=default_fill)
    elif hour == 8 or hour == 20:
        ex.canvas.itemconfigure(ex.eight, fill=default_fill)
    elif hour == 9 or hour == 21:
        ex.canvas.itemconfigure(ex.nine, fill=default_fill)
    elif hour == 10 or hour == 22:
        ex.canvas.itemconfigure(ex.ten2, fill=default_fill)
    elif hour == 11 or hour == 23:
        ex.canvas.itemconfigure(ex.eleven, fill=default_fill)
    elif hour == 12 or hour == 24 or hour == 0:
        ex.canvas.itemconfigure(ex.twelve, fill=default_fill)

    #am/pm/oclock
    if hour>12:
        ex.canvas.itemconfigure(ex.pm, fill=default_fill)
    elif hour == 12:
        ex.canvas.itemconfigure(ex.oclock, fill=default_fill)
    else:
        ex.canvas.itemconfigure(ex.am, fill=default_fill) 
        
    ex.canvas.after(10000,timer, ex)

    

def clear_all(ex):
    defualt_fill='#393939'
    ex.canvas.itemconfigure(ex.itis, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.half, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.ten1, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.quarter, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.twenty, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.five1, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.minutes, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.past, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.to, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.one, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.two, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.three, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.four, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.five2, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.six, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.seven, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.eight, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.nine, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.ten2, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.eleven, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.twelve, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.am, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.pm, fill=defualt_fill)
    ex.canvas.itemconfigure(ex.oclock, fill=defualt_fill)

def changeColor(ex, itemID):
    default_fill='#EAEAEA'
    ex.canvas.itemconfigure(itemID, fill=default_fill)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("820x780+300+300")
    root.after(1000,timer, ex)
    root.mainloop()

    
    


if __name__ == '__main__':
    main()
    
