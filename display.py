from tkinter import *
import encoder

class display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Message Encoder")
        self.geometry("500x300")
        self.resizable(0,0)
        Label(self, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
        msg = StringVar()
        key = StringVar()
        mode = StringVar()
        result = StringVar()
        def reset():
            msg.set("")
            key.set("")
            mode.set("encode")
            result.set("")
        Label(self, font= "arial 12 bold", text="MESSAGE").place(x= 60,y=60)
        Entry(self, font = "arial 10", textvariable = msg, bg = "ghost white").place(x=290, y = 60)
        Label(self, font = "arial 12 bold", text ="KEY").place(x=60, y = 90)
        Entry(self, font = "arial 10", textvariable = key , bg ="ghost white").place(x=290, y = 90)
        Label(self, font = "arial 12 bold", text ="MODE").place(x=60, y = 120)
        mode.set("encode")
        OptionMenu(self, mode, "encode", "decode").place(x=290, y = 120)
        def setResult():
            result.set(encoder.messageProcessor(mode, key, msg))
        Entry(self, font = "arial 10 bold", textvariable = result, bg ="ghost white", state="readonly").place(x=290, y = 150)
        Button(self, font = "arial 10 bold", text = "RESULT"  ,padx =2,bg ="LightGray" ,command = setResult).place(x=60, y = 150)
        Button(self, font = "arial 10 bold" ,text ="RESET" ,width =6, command = reset,bg = "LimeGreen", padx=2).place(x=80, y = 190)
        Button(self, font = "arial 10 bold",text= "EXIT" , width = 6, command = lambda: encoder.exit(self),bg = "OrangeRed", padx=2, pady=2).place(x=180, y = 190)
        self.mainloop()