from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        #Left label img
        img_top=Image.open("Images/help1.jpg")
        img_top=img_top.resize((1300,600),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1300,height=600)

        dev_label=Label(f_lbl, text="Email:patabalapravallika@gmail.com", font=("times new roman", 13, "bold"), bg="white")
        dev_label.place(x=510,y=350)
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()