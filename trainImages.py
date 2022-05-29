from cgitb import text
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
# from main import Face_Recognition_System


class TrainImages:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("train Images")

        
        butn_frame=Frame(self.root,bd=2,pady=3,relief=RIDGE,bg="white")
        butn_frame.place(x=0,y=200,width=660,height=100)

        back_button=Button(self.root,text="Back",command=self.Back_to_main,cursor="hand2")
        back_button.place(x=1265,y=100,width=90,height=30)

        train_Button=Button(butn_frame,command=self.trainClassifier,text="Train Data",font=("times new roman",13,"bold"),padx=10,width=14,bg="blue",fg="white")
        train_Button.grid(row = 0,column = 0)

        


    def trainClassifier(self):
        data_dir=("Student faces")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')    # gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



        # ************************* train classifier save****************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

    def Back_to_main(self):
        # self.old_window=Toplevel(self.root)
        # cv2.destroyAllWindows()
        self.root.destroy()
    






if __name__=="__main__":
    root=Tk()
    obj=TrainImages(root)
    root.mainloop()
