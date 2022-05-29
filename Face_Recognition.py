from cgitb import text
from inspect import CORO_CREATED
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np
import db_config
# from main import Face_Recognition_System


class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("train Images")

        back_button=Button(self.root,text="Back",command=self.Back_to_main,cursor="hand2")
        back_button.place(x=1265,y=100,width=90,height=30)

        
        butn_frame=Frame(self.root,bd=2,pady=3,relief=RIDGE,bg="white")
        butn_frame.place(x=0,y=200,width=660,height=100)

        train_Button=Button(butn_frame,command=self.recognition,text="Reconition",font=("times new roman",13,"bold"),padx=10,width=14,bg="blue",fg="white")
        train_Button.grid(row = 0,column = 0)



    # ******** Attandence ***********
    def mark_attendance(self,var_l,var_j,var_i,var_k):
        with open(r"attendance_details/Attandence__.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry= line.split((","))
                name_list.append(entry[0])
            if((var_l not in name_list) and (var_j not in name_list) and (var_i not in name_list ) and (var_k not in name_list )):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{var_l},{var_j},{var_i},{var_k},{dtString},{d1},Present\n")
                



    # ******* Face Recognition ************

    def recognition(self):
        def draw_boundray(img,classifire,scaleFactor,minNeighbors,color,text,clf):
            gray_images=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feachers=classifire.detectMultiScale(gray_images,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in feachers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_images[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                
                conn=mysql.connector.connect(host=db_config.MYSQL_HOST,username=db_config.MYSQL_USER,password=db_config.MYSQL_PASSWORD,database=db_config.MYSQL_DB)
                my_cursor=conn.cursor()

                my_cursor.execute("select name from new_table where ID="+str(id))
                var_i=my_cursor.fetchone()
                var_i="+".join(var_i)


                my_cursor.execute("select roll from new_table where ID="+str(id))
                var_j=my_cursor.fetchone()
                var_j="+".join(var_j)

                my_cursor.execute("select branch from new_table where ID="+str(id))
                var_k=my_cursor.fetchone()
                var_k="+".join(var_k)
                
                my_cursor.execute("select ID from new_table where ID="+str(id))
                var_l=my_cursor.fetchone()
                var_l="+".join(var_l)
            

                    











                if confidence>77:
            

                    cv2.putText(img,f"ID:{var_l}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{var_j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{var_i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"branch:{var_k}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(var_l,var_j,var_i,var_k)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def Back_to_main(self):
        # self.old_window=Toplevel(self.root)
        # cv2.destroyAllWindows()
        self.root.destroy()
    



if __name__=="__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()
