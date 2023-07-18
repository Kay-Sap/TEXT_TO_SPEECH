from tkinter import *
import pyttsx3
import threading

class App(Tk):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.geometry('800x425')
        self.title('Text_To_Speech')
        self.lbl = Label(self , text = "TEXT-TO-SPEECH" , font = ('timesroman',20,'bold'))
        self.lbl.pack()

        self.frame = LabelFrame(self ,takefocus=True)
        self.frame.place(x = 25, y = 70)
        self.text_area = Text(self.frame,borderwidth=1 , bg = '#79b6c7' ,width=60 , height=10,
                              font=('comic sans ms',15))

        self.btn = Button(self , text = 'RUN' , padx=20 , 
                          pady=10 , font = ('times roman',10,'bold'),command = self.functn)
        self.btn.place(x = 360 , y = 375)

        self.text_area.pack()
    
    def talk(self,txt):
        
        self.engine = pyttsx3.init()
        self.engine.say(txt)
        self.engine.runAndWait()
    
    def run(self):
        self.txt = self.text_area.get('1.0' , END)
        threading.Thread(target=self.talk(self.txt ))
        # self.talk(self.txt)

    def functn(self):

        self.cmd = self.text_area.get(index1='1.0' , index2=END)
        if self.cmd.strip() == '%setting':
            self.setting_page()
        else:
            self.talk(self.cmd)
    
             
    def setting_page(self):
        self.title('Setting')
        self.lbl.destroy()
        self.frame.destroy()
        self.btn.destroy()

        
 



if __name__ == '__main__':
    app = App()
    app.mainloop()
