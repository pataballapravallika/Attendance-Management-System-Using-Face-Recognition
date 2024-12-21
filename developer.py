from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        #Left label img
        img_top=Image.open("Images/dev1.jpg")
        img_top=img_top.resize((1380,600),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1380,height=600)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=600)

        img_top1=Image.open("Images/dev1.jpg")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top)
        f_lbl.place(x=300,y=40,width=280,height=200)

        dev_label=Label(main_frame, text="Hello my name, Pravallika", font=("times new roman", 13, "bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame, text="I'm a full stack developer", font=("times new roman", 13, "bold"), bg="white")
        dev_label.place(x=0,y=40)

        img1=Image.open(r"Images/fsd.jpg")
        img1=img1.resize((500,350),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(main_frame,image=self.photoimg1)
        f_lbl1.place(x=0,y=210,width=500,height=350)


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()