import customtkinter as ctk
from tkinter import  StringVar
from logic import Logic
ctk.set_appearance_mode("system")

### -- app -- ###

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.log = Logic()
        self.geometry("400x600")
        self.title("Calculator")
        self.configure(fg_color="#22252d")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.string = StringVar()
        self.string.set("")
        self.frame_label = ctk.CTkScrollableFrame(self , fg_color="black", orientation="horizontal",
                                                                        scrollbar_button_color="black")
        self.frame_label.grid(row = 0, column = 0, sticky = 'nsew' )

        self.frame_calc = ctk.CTkFrame(self, fg_color="black", bg_color="black")
        self.frame_calc.grid(row = 1, column = 0 , sticky = 'nsew', rowspan = 3)

        ### -- frame 1 elements -- ###
        self.label = ctk.CTkLabel(self.frame_label,fg_color="black", textvariable = self.string, font = ('arial', 25, 'bold'))
        self.label.grid( row = 0, column = 0 , pady = 60,padx= 15 , sticky = 'nsew')

        ### -- frame 2 grid -- ###
        self.frame_calc.grid_columnconfigure(0, weight=1)
        self.frame_calc.grid_columnconfigure(1, weight=1)
        self.frame_calc.grid_columnconfigure(2, weight=1)
        self.frame_calc.grid_columnconfigure(3, weight=1)
        self.frame_calc.grid_rowconfigure(0, weight = 1)
        self.frame_calc.grid_rowconfigure(1, weight = 1)
        self.frame_calc.grid_rowconfigure(2, weight = 1)
        self.frame_calc.grid_rowconfigure(3, weight = 1)
        self.frame_calc.grid_rowconfigure(4, weight = 1)

        ### -- frame 2 elements -- ###
        self.buttons = []

        for i in range(4):
            for j in range(4):
                self.bt = ctk.CTkButton(self.frame_calc, fg_color='#282b33',width=60, height=60,
                                        corner_radius=10, hover_color='#3c3f48')
                self.bt.grid(row = i, column = j, padx = 15, pady = 15, sticky = 'nsew')
                self.buttons.append(self.bt)

        self.bt0 = ctk.CTkButton(self.frame_calc, fg_color='#282b33',width=60, height=60, corner_radius=10,
                                 hover_color='#3c3f48', text="0",text_color="white", font=('arial', 28, 'bold') )
        self.bt0.grid(row = 4, column = 0, sticky = 'ew', columnspan = 2, padx = 15, pady = 10 )
        self.buttons.append(self.bt0)

        self.bt_dot = ctk.CTkButton(self.frame_calc, fg_color='#282b33',width=60, height=70, corner_radius=10,
                                    hover_color='#3c3f48',text=".",text_color="white", font=('arial', 28, 'bold'))
        self.bt_dot.grid(row = 4, column = 2,sticky = 'ew', pady = 15, padx = 15)
        self.buttons.append(self.bt_dot)

        self.bt_eq = ctk.CTkButton(self.frame_calc, fg_color='#f08221', width=60, height=60, corner_radius=10,
                                   hover_color='#3c3f48', text="=", text_color="white", font=('arial', 28, 'bold'))
        self.bt_eq.grid(row = 4, column = 3, sticky = 'nsew', padx= 15, pady = 15)
        self.buttons.append(self.bt_eq)
        self.bt_open = ctk.CTkButton(self,command=self.advanced_calc , fg_color="black", text="Advanced calculator",
                                     bg_color="black", hover_color="#2e2e2e")
        self.bt_open.grid(row = 0, column = 0, pady = (0, 150))

        self.num = 7
        for i in self.buttons[4:7]:
            i.configure(text = f"{self.num}", text_color="white", font=('arial', 28, 'bold'))
            self.num += 1

        self.num = 4
        for i in self.buttons[8:11]:
            i.configure(text=f"{self.num}", text_color="white", font=('arial', 28, 'bold'))
            self.num += 1

        self.num = 1
        for i in self.buttons[12:15]:
            i.configure(text=f"{self.num}", text_color="white", font=('arial', 28, 'bold'))
            self.num += 1

        self.symp = ["AC", "√", "÷", "⌫", "x", "+", "-"]
        self.num = 0
        for x in range(len(self.buttons)):
            if x in [0,1,2,3,7,11,15]:
                s = self.symp[self.num]
                self.buttons[x].configure(text = s,font=('arial', 22, 'bold'), text_color='#25fff8')
                self.num += 1

        self.button_keyboard_action = ["AC", "√", "÷", "⌫", "7", "8", "9", "x", "4", "5", "6", "+", "1", "2", "3", "-", "0", "."]
        self.butts = {}

        n = 0
        for i in range(18):
            s = self.button_keyboard_action[n]
            self.butts[s] = self.buttons[n]
            self.butts[s].configure(command=lambda v=s: self.out(v))
            n += 1
        self.butts["="] = self.bt_eq
        self.bind("<Key>", self.key_pressed)
        self.bind("<Return>", lambda event : self.butts["="].invoke())

        self.bt_eq.configure(command=self.eqq)
        self.is_eq = True

    def eqq(self):
        self.string.set(self.string.get() + "=")
        if self.string.get()[0] in ["÷", "x"] or self.string.get()[-2] in ["√", "÷", "x", "+", "-"]:
            self.label.configure(text_color="red")
            self.string.set("Error")
        else:
            self.log.str = self.string.get()
            print(self.log.str)
            try:
                s = self.log.math()
                current_text = self.string.set("")
                current_text = self.string.set(s)
                self.is_eq = False
            except ZeroDivisionError:
                self.label.configure(text_color="red")
                self.string.set("Error: cannot divide by 0")
            except Exception as e:
                self.label.configure(text_color="red")
                self.string.set(f"Error")
        self.is_eq = False



    def out(self, v ):
        self.label.configure(text_color="white")

        current_text = self.string.get()
        if self.is_eq :
            if v == "AC":
                current_text = self.string.set("")
            elif v == "⌫":
                current_text = self.string.set(current_text[:-1])
            else:
                self.string.set(current_text + v)
        else:
            if v == "AC":
                current_text = self.string.set("")
            elif v == "⌫":
                current_text = self.string.set(current_text[:-1])
            else:
                current_text = self.string.set("")
                current_text = self.string.get()
                self.string.set(current_text + v)
                self.is_eq = True

    def key_pressed(self, event):
        key = event.char
        if key == "÷":
            key = "/"
        if event.char == "/":
            self.butts["÷"].invoke()
        elif event.char == "*":
            self.butts["x"].invoke()
        elif key in self.butts:
            self.butts[key].invoke()
        elif event.keysym == "BackSpace":
            self.butts["⌫"].invoke()


    def advanced_calc(self):
        self.frame_calc.grid_columnconfigure(4, weight = 1)
        self.frame_calc.grid_columnconfigure(5, weight = 1)
        self.bt_open.destroy()
        self.geometry("500x600")
        for i in range(len(self.buttons)):
            if i in [3, 7, 11, 15, 18]:
                self.buttons[i].grid_configure(column = 3)
        self.bt_eq.grid_configure(column = 4,columnspan=2, sticky='ew')
        self.bt_dot.grid_configure(columnspan=2)


        num  = 0
        self.sympol = ["(", "xˣ", "!", "Tan(", ")", "Cos(", "Sin(", "log("]
        for i in range(4):
            s  =self.sympol[num]
            self.but = ctk.CTkButton(self.frame_calc, width=60, height=60, corner_radius=10,
                                     command= lambda v = s: self.out(v),hover_color='#3c3f48',
                                     font=('arial', 22, 'bold'), fg_color='#282b33', text = self.sympol[num])
            self.but.grid(row = i, column = 4 ,padx = 15, pady = 15, sticky = 'ew')
            self.buttons.append(self.but)
            self.butts[s] = self.but
            num += 1
        for i in range(4):
            s = self.sympol[num]
            self.but = ctk.CTkButton(self.frame_calc, width=60, height=60, corner_radius=10,
                                     command= lambda v = s : self.out(v), hover_color='#3c3f48', font=('arial', 14, 'bold'),
                                     fg_color='#282b33', text = self.sympol[num])
            self.but.grid(row = i, column = 5 ,padx = 15, pady = 15, sticky = 'ew')
            self.buttons.append(self.but)
            self.butts[s] = self.but
            num+=1
        self.buttons[23].configure(font=('arial', 22, 'bold'))
        self.buttons[20].configure(command= lambda v = "^" : self.out(v))
        self.buttons[22].configure(font=('arial', 14, 'bold'),command= lambda v = "Tan(" : self.out(v))




main = Main()
main.mainloop()
