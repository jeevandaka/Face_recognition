
from tkinter import*
from tkinter import ttk
from cgitb import text
import tkinter
from tkinter import messagebox
import os
from tkinter.font import BOLD  # for stylish tool kit
from PIL import Image,ImageTk
from Face_Recognition import face_recognition 
from studentDetail import Student
from trainImages import TrainImages
from attendance import attendance_



class Face_Recognition_System:
    def __init__(self,root) -> None:
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        
        img = Image.open(r"images for project/background_face-1200x480.jpg")
        img= img.resize((1370,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=1370,height=150)

        # backgraund Image
        img1 = Image.open(r"images for project/images.png")
        img1= img1.resize((1370,1000),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl1=Label(self.root,image=self.photoimg1)
        first_lbl1.place(x=0,y=150,width=1370,height=1000)


        title_lbl = Label(first_lbl1,text="Welcome",font=("times new roman",35,"bold"))
        title_lbl.place(x=0,y=0,width=1370,height=40)

        
        #Button for studen details
        Stu_Detail_img = Image.open(r"images for project/download.png")
        Stu_Detail_img= Stu_Detail_img.resize((200,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(Stu_Detail_img)

        first_bt1=Button(first_lbl1,image=self.photoimg4,command=self.student_details,cursor="hand2")
        first_bt1.place(x=100,y=100,width=200,height=150)

        first_bt1_1=Button(first_lbl1,text="Student Details",command=self.student_details,cursor="hand2")
        first_bt1_1.place(x=100,y=250,width=200,height=30)


        # button for image recognition
        img2 = Image.open(r"images for project/images (1).jpg")
        img2= img2.resize((200,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_bt=Button(first_lbl1,image=self.photoimg2,command=self.Face__Recognition,cursor="hand2")
        first_bt.place(x=400,y=100,width=200,height=150)

        first_bt_=Button(first_lbl1,text="Face Recognition",command=self.Face__Recognition,cursor="hand2")
        first_bt_.place(x=400,y=250,width=200,height=30)

        # button to see attendance
        img3 = Image.open(r"images for project/attendance.png")
        img3= img3.resize((200,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        first_bt2=Button(first_lbl1,image=self.photoimg3,command=self.student_attendance,cursor="hand2")
        first_bt2.place(x=700,y=100,width=200,height=150)

        first_bt2_=Button(first_lbl1,text="Attendance",command=self.student_attendance,cursor="hand2")
        first_bt2_.place(x=700,y=250,width=200,height=30)


        # Chat robot
        img4 = Image.open(r"images for project/student_photo.png")
        img4= img4.resize((200,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img4)

        first_bt3=Button(first_lbl1,image=self.photoimg5,command=self.open_img,cursor="hand2")
        first_bt3.place(x=1000,y=100,width=200,height=150)

        first_bt3_=Button(first_lbl1,text="Scaned Photos",command=self.open_img,cursor="hand2")
        first_bt3_.place(x=1000,y=250,width=200,height=30)

        #Train Data
        img5 = Image.open(r"images for project/details.jpg")
        img5= img5.resize((200,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img5)

        first_bt4=Button(first_lbl1,image=self.photoimg6,command=self.train_Images,cursor="hand2")
        first_bt4.place(x=400,y=300,width=200,height=150)

        first_bt4_=Button(first_lbl1,text="Train Data",command=self.train_Images,cursor="hand2")
        first_bt4_.place(x=400,y=450,width=200,height=30)


        #Exit
        img6 = Image.open(r"images for project/download (1).png")
        img6= img6.resize((200,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img6)

        first_bt5=Button(first_lbl1,image=self.photoimg7,command=self.Exit__,cursor="hand2")
        first_bt5.place(x=700,y=300,width=200,height=150)

        first_bt5_=Button(first_lbl1,text="Exit",command=self.Exit__,cursor="hand2")
        first_bt5_.place(x=700,y=450,width=200,height=30)



    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_Images(self):
        self.new_window=Toplevel(self.root)
        self.app=TrainImages(self.new_window)

    def Face__Recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def Exit__(self):
        self.Exit__=messagebox.askyesno("Face Recognition","Are you sure exit this project")
        if self.Exit__>0:
            self.root.destroy()

    
    def student_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_(self.new_window)

    def open_img(self):
        os.startfile("Student faces")




if __name__=="__main__":
    root=Tk()
    object=Face_Recognition_System(root)
    root.mainloop()