from cgitb import text
from operator import mod
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tokenize import String
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog
import cv2
# from main import Face_Recognition_System

mydata=[]

class attendance_:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")

        # ****************** Variables **************
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_branch=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        




        img = Image.open(r"images for project/student_information.png")
        img= img.resize((1370,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=1370,height=200)

        # backgraund Image
        img1 = Image.open(r"images for project/images.png")
        img1= img1.resize((1370,1000),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl1=Label(self.root,image=self.photoimg1)
        first_lbl1.place(x=0,y=200,width=1370,height=1000)


        title_lbl = Label(first_lbl1,text="ATTENDANCE MAMAGEMENT SYSTEM",bg="white",font=("times new roman",30,"bold"))
        title_lbl.place(x=0,y=0,width=1370,height=30)

        back_button=Button(first_lbl1,text="Back",command=self.Back_to_main,cursor="hand2")
        back_button.place(x=1265,y=0,width=90,height=30)


        # main frame
        mainFrame = Frame(first_lbl1,bd=2,bg="white")
        mainFrame.place(x=20,y=40,width=1320,height=450)

        # left label frame
        leftLabelFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        leftLabelFrame.place(x=10,y=5,width=680,height=430)


        img_info = Image.open(r"images for project/attendance-tracking-and-managing-software.jpg")
        img_info= img_info.resize((680,150),Image.ANTIALIAS)
        self.photoimg_info=ImageTk.PhotoImage(img_info)

        first_lbl=Label(leftLabelFrame,image=self.photoimg_info)
        first_lbl.place(x=0,y=0,width=680,height=150)


        currentStudentFrame= LabelFrame(leftLabelFrame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        currentStudentFrame.place(x=5,y=150,width=670,height=255)

        # Student id information
        studentIdLabel = Label(currentStudentFrame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentIdLabel.grid(row=0,column=0,padx=10,sticky=W)

        studentIdEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        studentIdEntry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Student name 
        studentNameLabel = Label(currentStudentFrame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentNameLabel.grid(row=0,column=2,padx=10,sticky=W)

        studentNameEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        studentNameEntry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Enrollment Number 
        inrollmentNumberLabel = Label(currentStudentFrame,text="Enrollment number:",font=("times new roman",12,"bold"),bg="white")
        inrollmentNumberLabel.grid(row=1,column=0,padx=10,sticky=W)

        inrollmentNumberEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        inrollmentNumberEntry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Branch 
        classDivisionLabel = Label(currentStudentFrame,text="Branch:",font=("times new roman",12,"bold"),bg="white")
        classDivisionLabel.grid(row=1,column=2,padx=10,sticky=W)

        DivisionIdEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_branch,width=20,font=("times new roman",12,"bold"))
        DivisionIdEntry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Time
        DOBLabel = Label(currentStudentFrame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        DOBLabel.grid(row=2,column=0,padx=10,sticky=W)

        DOBEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        DOBEntry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
        # Date
        genderLabel = Label(currentStudentFrame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        genderLabel.grid(row=2,column=2,padx=10,sticky=W)

        genderEntry = ttk.Entry(currentStudentFrame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        genderEntry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



        AttendanceLable = Label(currentStudentFrame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        AttendanceLable.grid(row=3,column=0,padx=10)

        attendanceCombo = ttk.Combobox(currentStudentFrame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        attendanceCombo["values"]=("Status","Present","Absent")
        attendanceCombo.current(0)
        attendanceCombo.grid(row=3,column=1,padx=2,pady=10,sticky=W)


        # update or save buttons frame
        butn_frame=Frame(currentStudentFrame,bd=2,pady=3,relief=RIDGE,bg="white")
        butn_frame.place(x=0,y=170,width=660,height=45)
        
        
        Import_Button=Button(butn_frame,text="Import csv",command=self.importCsv,font=("times new roman",13,"bold"),padx=10,width=14,bg="blue",fg="white")
        Import_Button.grid(row = 0,column = 0)


        export_Button=Button(butn_frame,text="Exort csv",command=self.exportCsv,font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        export_Button.grid(row = 0,column = 1)

        update_Button=Button(butn_frame,text="Update",font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        update_Button.grid(row = 0,column = 2)


        reset_Button=Button(butn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=14,bg="blue",fg="white")
        reset_Button.grid(row = 0,column = 3)


    # right label frame
        rightLabelFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        rightLabelFrame.place(x=700,y=5,width=600,height=430)



    
    # *********** Table frame ************

        tableFrame=Frame(rightLabelFrame,bd=2,bg="white",relief=RIDGE)
        tableFrame.place(x=5,y=0,width=590,height=410)

        scroll_x=Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(tableFrame,orient=VERTICAL)

        self.studentTable = ttk.Treeview(tableFrame,column=("id","roll","name","branch","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)

        self.studentTable.heading("id",text="Student ID")
        self.studentTable.heading("roll",text="Enrollment")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("branch",text="Branch")
        self.studentTable.heading("time",text="Time")
        self.studentTable.heading("date",text="Date")
        self.studentTable.heading("attendance",text="Attendance Status")
        self.studentTable["show"]="headings"

        self.studentTable.column("id",width=100)
        self.studentTable.column("roll",width=100)
        self.studentTable.column("name",width=100)
        self.studentTable.column("branch",width=100)
        self.studentTable.column("time",width=100)
        self.studentTable.column("date",width=100)
        self.studentTable.column("attendance",width=100)
        
        

        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.studentTable.delete(*self.studentTable.get_children())
        for i in rows:
            self.studentTable.insert("",END,values=i)


# import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fileName=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fileName) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fileName=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fileName,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fileName)+" Successfully")
            # self.fetchData(mydata)
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

        
    def get_cursor(self,event=""):
        cursor_row=self.studentTable.focus()
        content=self.studentTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_roll.set(rows[2])
        self.var_atten_branch.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_branch.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    def Back_to_main(self):
        # self.old_window=Toplevel(self.root)
        # cv2.destroyAllWindows()
        self.root.destroy()


        

if __name__=="__main__":
    root=Tk()
    obj=attendance_(root)
    root.mainloop()
